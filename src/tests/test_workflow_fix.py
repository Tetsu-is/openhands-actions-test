#!/usr/bin/env python3
"""
Test for the headless workflow fix.
This test validates that the GitHub Actions workflow is properly configured.
"""

import yaml
import os
import unittest

class TestWorkflowFix(unittest.TestCase):
    """Test cases for the headless workflow fix."""

    def setUp(self):
        """Set up test fixtures."""
        self.workflow_path = '.github/workflows/openhands-headless.yml'
        self.root_path = os.path.join(os.path.dirname(__file__), '..', '..')
        self.full_workflow_path = os.path.join(self.root_path, self.workflow_path)

    def test_workflow_file_exists(self):
        """Test that the workflow file exists."""
        self.assertTrue(os.path.exists(self.full_workflow_path),
                       f"Workflow file should exist at {self.workflow_path}")

    def test_workflow_yaml_syntax(self):
        """Test that the workflow file has valid YAML syntax."""
        with open(self.full_workflow_path, 'r') as f:
            try:
                workflow = yaml.safe_load(f)
                self.assertIsInstance(workflow, dict, "Workflow should be a valid YAML dictionary")
            except yaml.YAMLError as e:
                self.fail(f"Workflow YAML syntax is invalid: {e}")

    def test_workflow_structure(self):
        """Test that the workflow has the correct structure."""
        with open(self.full_workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)

        # Check basic structure
        self.assertIn('name', workflow, "Workflow should have a name")
        self.assertTrue(True in workflow or 'on' in workflow, "Workflow should have trigger section")
        self.assertIn('jobs', workflow, "Workflow should have jobs section")
        self.assertIn('permissions', workflow, "Workflow should have permissions section")

    def test_job_condition_syntax(self):
        """Test that the job condition has correct syntax (no space after 'if')."""
        with open(self.full_workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)

        job = workflow['jobs']['run-headless-mode']
        self.assertIn('if', job, "Job should have 'if' condition")

        # The condition should be properly formatted
        condition = job['if'].strip()
        expected_condition = "github.event.label.name == 'headless'"
        self.assertEqual(condition, expected_condition,
                        f"Job condition should be '{expected_condition}'")

    def test_trigger_events(self):
        """Test that all required trigger events are configured."""
        with open(self.full_workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)

        # Get triggers (YAML parser treats 'on' as boolean True)
        triggers = workflow[True] if True in workflow else workflow.get('on', {})

        required_triggers = [
            'issues', 'pull_request', 'issue_comment',
            'pull_request_review_comment', 'pull_request_review'
        ]

        for trigger in required_triggers:
            self.assertIn(trigger, triggers, f"Missing trigger: {trigger}")

        # Check that labeled events are configured for issues and pull_request
        for trigger in ['issues', 'pull_request']:
            self.assertIn('types', triggers[trigger], f"{trigger} should have types")
            self.assertIn('labeled', triggers[trigger]['types'],
                         f"{trigger} should include 'labeled' type")

    def test_permissions(self):
        """Test that required permissions are configured."""
        with open(self.full_workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)

        permissions = workflow.get('permissions', {})
        required_permissions = ['contents', 'pull-requests', 'issues']

        for perm in required_permissions:
            self.assertIn(perm, permissions, f"Missing permission: {perm}")
            self.assertEqual(permissions[perm], 'write',
                           f"Permission {perm} should be 'write'")

    def test_environment_variable_setup(self):
        """Test that environment variables are properly set up."""
        with open(self.full_workflow_path, 'r') as f:
            content = f.read()

        # Check that ISSUE_TYPE is set
        self.assertIn('ISSUE_TYPE=pr', content, "Should set ISSUE_TYPE=pr for pull requests")
        self.assertIn('ISSUE_TYPE=issue', content, "Should set ISSUE_TYPE=issue for issues")

        # Check that ISSUE_NUMBER is set
        self.assertIn('ISSUE_NUMBER=', content, "Should set ISSUE_NUMBER")

        # Check that environment variables are used
        self.assertTrue(
            'process.env.ISSUE_TYPE' in content or '${{ env.ISSUE_TYPE }}' in content,
            "Should use ISSUE_TYPE environment variable"
        )
        self.assertIn('${{ env.ISSUE_NUMBER }}', content, "Should use ISSUE_NUMBER environment variable")

if __name__ == '__main__':
    unittest.main()
