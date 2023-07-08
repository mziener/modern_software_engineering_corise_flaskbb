# CoRise TODO: create a new log group
#

resource "aws_cloudwatch_log_group" "flaskbb_app" {
  name = "flaskbb_app"
}

# CoRise TODO: create a new dashboard
resource "aws_cloudwatch_dashboard" "flaskbb_main" {
  dashboard_name = "flaskbb_main"

  dashboard_body = jsonencode({
    "widgets" : [
      {
        "type" : "metric",
        "x" : 0,
        "y" : 0,
        "width" : 6,
        "height" : 6,
        "properties" : {
          "view" : "timeSeries",
          "stacked" : false,
          "metrics" : [
            ["flaskbb_app", "$forum/index_visitor_count"]
          ],
          "region" : "eu-north-1"
        }
      },
      {
        "type" : "metric",
        "x" : 6,
        "y" : 0,
        "width" : 6,
        "height" : 6,
        "properties" : {
          "view" : "timeSeries",
          "stacked" : true,
          "metrics" : [
            ["AWS/ElasticBeanstalk", "ApplicationRequestsTotal", "EnvironmentName", "flaskbb-environment"],
            [".", "ApplicationRequests5xx", ".", "."],
            [".", "ApplicationRequests4xx", ".", "."],
            [".", "ApplicationRequests2xx", ".", "."]
          ],
          "region" : "eu-north-1"
        }
      },
      {
        "type" : "metric",
        "x" : 12,
        "y" : 0,
        "width" : 6,
        "height" : 6,
        "properties" : {
          "view" : "timeSeries",
          "stacked" : false,
          "metrics" : [
            ["flaskbb_app", "$auth/register_visitor_count"]
          ],
          "region" : "eu-north-1"
        }
      },
      {
        "type" : "metric",
        "x" : 0,
        "y" : 6,
        "width" : 24,
        "height" : 6,
        "properties" : {
          "sparkline" : true,
          "view" : "singleValue",
          "metrics" : [
            ["AWS/ElasticBeanstalk", "ApplicationRequests5xx", "EnvironmentName", "flaskbb-environment"],
            [".", "InstancesNoData", ".", "."],
            [".", "InstancesPending", ".", "."],
            [".", "InstancesOk", ".", "."],
            [".", "InstancesWarning", ".", "."],
            [".", "InstancesDegraded", ".", "."],
            [".", "InstancesSevere", ".", "."],
            [".", "ApplicationLatencyP99.9", ".", "."],
            [".", "ApplicationLatencyP99", ".", "."],
            [".", "ApplicationLatencyP95", ".", "."],
            [".", "ApplicationRequestsTotal", ".", "."],
            [".", "ApplicationRequests4xx", ".", "."]
          ],
          "region" : "eu-north-1"
        }
      }
    ]
  })
}

#CoRise TODO: create metric alters
resource "aws_cloudwatch_metric_alarm" "bot_attack" {

  alarm_name          = "bot_attack"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "$auth/register_visitor_count"
  namespace           = "flaskbb_app"
  period              = 60
  statistic           = "Sum"
  threshold           = 10

}

resource "aws_cloudwatch_metric_alarm" "too_busy" {
  alarm_name          = "too_busy"
  comparison_operator = "LessThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "CPUIdle"
  namespace           = "AWS/ElasticBeanstalk"
  period              = 300
  statistic           = "Average"
  threshold           = 50
}
