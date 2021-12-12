Feature: Rate, Errors and Duration (RED) Metrics
  Scenario Outline: Test Metrics
    Given a metrics object
    When <actual_transactions> transactions are applied
    And <actual_errors> errors are applied
    And <actual_duration> duration in seconds is applied
    Then ensure rate matches <expected_rate>
    And ensure errors matches <expected_errors>
    And ensure duration is greater than or equal to <expected_duration>
    And ensure string representation is valid
    Examples:
      | actual_transactions | actual_errors | actual_duration | expected_rate | expected_errors | expected_duration |
      | 0                   | 0             | 1               | 0             | 0               | 0                 |
      | 1                   | 1             | 1               | 1             | 1               | 1000              |
      | 1,2,3               | 1,2,3         | 3               | 6             | 6               | 500               |

    Scenario Outline: Rate Throttling
      Given a rate of <rate>
      When transaction count is <count>
      Then throttle time should be greater or equal to <throttle_time>
      Examples:
        | rate | count | throttle_time |
        | 120  | 119   | 0.5           |
        | 120  | 2     | 0.0           |
        | 120  | 0     | 0.0           |
