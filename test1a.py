'''Convert XE to Meraki by Bryn Pounds'''
import requests

true="True"
false = "False"
null="Null"

nso_json={
  "data": {
    "tailf-ncs:devices": {
      "device": [
        {
          "name": "23adca9a-a681-453f-b46e-333bfcd49d2c",
          "config": {
            "tailf-ned-cisco-ios:interface": {
              "GigabitEthernet": [
                {
                  "name": "0/0",
                  "negotiation": {
                    "auto": true
                  },
                  "speed": "1000",
                  "vrf": {
                    "forwarding": "Mgmt-vrf"
                  },
                  "ip": {
                    "no-address": {
                      "address": false
                    }
                  },
                  "shutdown": [null]
                },
                {
                  "name": "1/0/1",
                  "switchport": {
                    "mode": {
                      "access": {
                      }
                    }
                  },
                  "power": {
                    "inline": {
                      "mode": "never"
                    }
                  }
                },
                {
                  "name": "1/0/10",
                  "switchport": {
                    "mode": {
                      "access": {
                      }
                    },
                    "access": {
                      "vlan": 11
                    },
                    "voice": {
                      "vlan": 20
                    }
                  },
                  "spanning-tree": {
                    "portfast": {
                    }
                  }
                },
                {
                  "name": "1/0/11",
                  "speed": "100",
                  "duplex": "half"
                },
                {
                  "name": "1/0/12",
                  "switchport": {
                    "mode": {
                      "access": {
                      }
                    },
                    "access": {
                      "vlan": 72
                    }
                  },
                  "speed": "10",
                  "duplex": "full"
                },
                {
                  "name": "1/0/13"
                },
                {
                  "name": "1/0/14"
                },
                {
                  "name": "1/0/15"
                },
                {
                  "name": "1/0/16"
                },
                {
                  "name": "1/0/17"
                },
                {
                  "name": "1/0/18"
                },
                {
                  "name": "1/0/19"
                },
                {
                  "name": "1/0/2"
                },
                {
                  "name": "1/0/20"
                },
                {
                  "name": "1/0/21",
                  "spanning-tree": {
                    "bpduguard": {
                      "enable": [null]
                    },
                    "guard": "root"
                  },
                  "speed": "10"
                },
                {
                  "name": "1/0/22",
                  "spanning-tree": {
                    "bpdufilter": "enable",
                    "guard": "loop"
                  },
                  "speed": "100"
                },
                {
                  "name": "1/0/23",
                  "spanning-tree": {
                    "bpduguard": {
                      "enable": [null]
                    },
                    "guard": "root"
                  },
                  "speed": "1000"
                },
                {
                  "name": "1/0/24",
                  "spanning-tree": {
                    "bpduguard": {
                      "enable": [null]
                    },
                    "guard": "root"
                  },
                  "speed": "10",
                  "duplex": "full"
                },
                {
                  "name": "1/0/25",
                  "speed": "10",
                  "duplex": "half"
                },
                {
                  "name": "1/0/26",
                  "speed": "100",
                  "duplex": "full"
                },
                {
                  "name": "1/0/27",
                  "speed": "100",
                  "duplex": "full"
                },
                {
                  "name": "1/0/28",
                  "speed": "1000"
                },
                {
                  "name": "1/0/29"
                },
                {
                  "name": "1/0/3"
                },
                {
                  "name": "1/0/30"
                },
                {
                  "name": "1/0/31"
                },
                {
                  "name": "1/0/32"
                },
                {
                  "name": "1/0/33"
                },
                {
                  "name": "1/0/34"
                },
                {
                  "name": "1/0/35"
                },
                {
                  "name": "1/0/36"
                },
                {
                  "name": "1/0/37"
                },
                {
                  "name": "1/0/38"
                },
                {
                  "name": "1/0/39"
                },
                {
                  "name": "1/0/4"
                },
                {
                  "name": "1/0/40"
                },
                {
                  "name": "1/0/41"
                },
                {
                  "name": "1/0/42"
                },
                {
                  "name": "1/0/43"
                },
                {
                  "name": "1/0/44"
                },
                {
                  "name": "1/0/45"
                },
                {
                  "name": "1/0/46"
                },
                {
                  "name": "1/0/47"
                },
                {
                  "name": "1/0/48"
                },
                {
                  "name": "1/0/5",
                  "switchport": {
                    "mode": {
                      "trunk": {
                      }
                    },
                    "trunk": {
                      "native": {
                        "vlan": 75
                      }
                    }
                  },
                  "spanning-tree": {
                    "bpdufilter": "enable",
                    "bpduguard": {
                      "enable": [null]
                    }
                  },
                  "speed": "100"
                },
                {
                  "name": "1/0/6",
                  "description": "My switch port",
                  "switchport": {
                    "access": {
                      "vlan": 10
                    }
                  },
                  "spanning-tree": {
                    "bpduguard": {
                      "enable": [null]
                    }
                  },
                  "storm-control": {
                    "unicast": {
                      "level-threshold": {
                        "level": {
                          "rising": "87.0",
                          "falling": "65.0"
                        }
                      }
                    }
                  },
                  "udld": {
                    "port": {
                    }
                  }
                },
                {
                  "name": "1/0/7"
                },
                {
                  "name": "1/0/8",
                  "shutdown": [null]
                },
                {
                  "name": "1/0/9",
                  "switchport": {
                    "mode": {
                      "trunk": {
                      }
                    },
                    "trunk": {
                      "allowed": {
                        "vlan": {
                          "vlans": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                        }
                      }
                    }
                  }
                },
                {
                  "name": "1/1/1"
                },
                {
                  "name": "1/1/2"
                },
                {
                  "name": "1/1/3"
                },
                {
                  "name": "1/1/4"
                }
              ],
              "TenGigabitEthernet": [
                {
                  "name": "1/1/1"
                },
                {
                  "name": "1/1/2"
                },
                {
                  "name": "1/1/3"
                },
                {
                  "name": "1/1/4"
                },
                {
                  "name": "1/1/5"
                },
                {
                  "name": "1/1/6"
                },
                {
                  "name": "1/1/7"
                },
                {
                  "name": "1/1/8"
                }
              ],
              "TwentyFiveGigE": [
                {
                  "name": "1/1/1"
                },
                {
                  "name": "1/1/2"
                }
              ],
              "FortyGigabitEthernet": [
                {
                  "name": "1/1/1"
                },
                {
                  "name": "1/1/2"
                }
              ],
              "Vlan": [
                {
                  "name": 1,
                  "ip": {
                    "address": {
                      "dhcp": {
                      }
                    }
                  },
                  "ipv6": {
                    "address": {
                      "autoconfig": {
                      }
                    },
                    "enable": [null],
                    "nd": {
                      "autoconfig": {
                        "default-route": [null]
                      }
                    }
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}


#for item in nso_json['data']['tailf-ncs:devices']['device'][0]['config']['tailf-ned-cisco-ios:interface']['GigabitEthernet']:
    #print(item)
    
"""
{
    "name": "My switch port",
    "tags": "tag1 tag2",
    "enabled": true,
    "poeEnabled": true,
    "type": "access",
    "vlan": 10,
    "voiceVlan": 20,
    "isolationEnabled": false,
    "rstpEnabled": true,
    "stpGuard": "disabled",
    "accessPolicyNumber": "1234",
    "linkNegotiation": "Auto negotiate",
    "portScheduleId": "1234",
    "udld": "Alert only",
    "macWhitelist": [
        "34:56:fe:ce:8e:a0",
        "34:56:fe:ce:8e:a1"
    ],
    "stickyMacWhitelist": [
        "34:56:fe:ce:8e:b0",
        "34:56:fe:ce:8e:b1"
    ],
    "stickyMacWhitelistLimit": 5,
    "stormControlEnabled": true
}
"""



pre_payload = '''{'''
post_payload = '''}'''

meraki_ports=[]
for number in range(len(ports)):
    meraki_ports.append("")
    
for index, port in enumerate(ports):
    if "description" in port:
        meraki_ports[index] += '''"name":"''' + port['description'] + '''",'''
    if "shutdown" in port:
        meraki_ports[index] += '''"enabled": false,'''
    if "power" in port:
        meraki_ports[index] += '''"poeEnabled" : false,'''
    if "switchport" in port:
        #print(index, port['switchport'])
        #if "access"in port['switchport'] and not "mode" in port['switchport']:
            #print("vlan is " + str(port['switchport']['access']['vlan']))
        if "mode" in port['switchport']:
            meraki_ports[index] += '''"type": "''' + str(port['switchport']['mode'])[2:-6] + '''",'''
            try:
                meraki_ports[index] += '''"vlan": ''' + str(port['switchport']['access']['vlan']) + ''','''
            except:
                meraki_ports[index] += '''"vlan": 1,'''
            try:
                meraki_ports[index] += '''"voiceVlan": ''' + str(port['switchport']['voice']['vlan']) + ''','''
            except:
                pass
    if "speed" in port:
        if port['speed'] == "1000":
            meraki_ports[index] += '''"linkNegotiation" : "1 Gigabit full duplex (forced)",'''
        if "speed" and "duplex" in port:
            meraki_ports[index] += '''"linkNegotiation" : "''' + port['speed'] + ''' Megabit ''' + port['duplex'] + ''' duplex (forced)",'''     
        if "speed" and not "duplex" in port:
            if port['speed']  != "1000":
                meraki_ports[index] += '''"linkNegotiation" : "''' + port['speed'] + ''' Megabit (auto)",''' 
    if "spanning-tree" in port:
        if "bpduguard" in port['spanning-tree']:
            meraki_ports[index] += '''"stpGuard": "bpdu guard",'''
        if "spanning-tree" in port and "guard" in port['spanning-tree']:
            if port['spanning-tree']['guard'] == "root":
                meraki_ports[index] += '''"stpGuard": "root guard",'''
            if port['spanning-tree']['guard'] == "loop":
                meraki_ports[index] += '''"stpGuard": "loop guard",'''

                    
                    
for index, port in enumerate(meraki_ports):
    if port:
        payload = pre_payload + port + post_payload
        payload = payload[:-2] + '''}'''
        print("Meraki Port " + str(index) + " payload: ", payload)
    
