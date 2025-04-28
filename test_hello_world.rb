# test_hello_world.rb

require 'minitest/autorun'

class TestHelloWorld < Minitest::Test
  def test_output
    assert_output("Hello World\n") { load './hello_world.rb' }
  end
end
