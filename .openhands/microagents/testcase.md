---
triggers:
- testcase
---

The functionality seems to be okay. We don't need additional implementation. We should care about test code.

The user wants to check if he provide sufficient testcases to ensure the functionality he implemented.
Your duty is check if there are enough testcases.

In addition to the general review of test cases, it is crucial to meticulously examine those that cover threshold or boundary conditions. When functionality behaves differently based on certain limits (e.g., minimum/maximum values, specific cut-off points), ensure comprehensive testing around these thresholds. This includes test cases with values exactly at the threshold, just below it, and just above it. Such scrutiny helps uncover potential off-by-one errors or incorrect logic at critical transition points, ensuring the implemented functionality is robust and behaves as expected under all relevant boundary scenarios.
