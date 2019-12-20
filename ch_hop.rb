#!/usr/bin/env ruby
IFACE = "wlan1"
IEEE80211bg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
IEEE80211bg_intl = IEEE80211bg + [12, 13, 14]
IEEE80211a = [36, 40, 44, 48, 52, 56, 60, 64,149, 153, 157, 161]
IEEE80211bga = IEEE80211bg + IEEE80211a
IEEE80211bga_intl = IEEE80211bg_intl + IEEE80211a
CHANNEL_PERIOD = 0.1

while true
    IEEE80211bg.each do |channel|
        `iwconfig #{IFACE} channel #{channel}`
        sleep CHANNEL_PERIOD
    end
end

