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
