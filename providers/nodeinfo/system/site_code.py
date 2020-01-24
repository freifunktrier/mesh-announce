import providers
import socket

sites = { 'bat0':'seg_00', 'bat01':'seg_01', 'bat02':'seg_02', 'bat03':'seg_03', 'bat04':'seg_04', 'bat05':'seg_05'}

class Source(providers.DataSource):
    def required_args(self):
        return ['batadv_dev']

    def call(self, batadv_dev):
        return sites[batadv_dev]
