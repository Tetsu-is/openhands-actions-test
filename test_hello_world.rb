# test_hello_world.rb

require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_output
    output = `ruby hello_world.rb`
    assert_equal "Hello World\n", output
  end
end
