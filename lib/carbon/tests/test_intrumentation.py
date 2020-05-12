from carbon.instrumentation import increment, CarbonMetricsCollector, stats, recordMetrics, DATAPOINTS_RECEIVED
from prometheus_client import REGISTRY
from unittest import TestCase


class TestPrometheusMetrics(TestCase):

  def setUp(self):
    # necessary for recordMetric to work
    from carbon.conf import settings
    settings['program'] = 'test'
    settings['instance'] = None

  def test_metricsRecieved(self):
    stats.clear()
    increment("metricsReceived")
    recordMetrics()
    self.assertCurrentDPValue(1)
    increment("metricsReceived")
    self.assertCurrentDPValue(1)
    recordMetrics()
    self.assertCurrentDPValue(2)

  def assertCurrentDPValue(self, value):
    self.assertEqual(value, REGISTRY.get_sample_value('carbon_datapoints_received_total'))
