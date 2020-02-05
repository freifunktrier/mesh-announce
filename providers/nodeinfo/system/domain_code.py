import providers
import socket

domains = { 'bat0':'fftr_GW', 'bat01':'fftr_GW', 'bat02':'fftr_GW', 'bat03':'fftr_GW', 'bat04':'fftr_GW', 'bat05':'fftr_GW'}

class Source(providers.DataSource):
    def cache_ttl(self):
        return 0
    
    def required_args(self):
        return ['batadv_dev']

    def call(self, batadv_dev):
        return domains[batadv_dev]
