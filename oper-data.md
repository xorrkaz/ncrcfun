# Operational Data

Operational Data for a network element can be defined as what an element is doing. Translation; 'what is the value of a specific operational characteristic?'. This type of question strives to be answered with techniques like SNMP; via polling. In others words, if a piece of software needs data from another system, it will go ask the system for that value and expect it to be returned.

Did you know NETCONF and RESTCONF can derive similar outcomes? Did you know you can parse data as easily with operational data as you can with configuration data? Operational Data (or oper-data) can do this. oper-data can be asked for (polled) or soon put on a message bus where subscriptions and publications are established with no need to poll. See [here](https://developer.cisco.com/site/ios-xe/docs/#streaming-telemetry-quick-start-guide) for more data on streaming telemetry.

## Pre-requisites

See [here](https://developer.cisco.com/site/ios-xe/docs/index.gsp#enabling-netconf-on-ios-xe) for NETCONF or [here](https://developer.cisco.com/site/ios-xe/docs/index.gsp#enabling-restconf-on-ios-xe) for RESTCONF. In summary, you need **netconf-yang** and/or **restconf** enabled on your network element.

## Default oper-data

As of IOS-XE 16.5, several data structures can be derived for oper-data, without any additional configurations or steps. They are as follows:
* [Cisco-IOS-XE-acl-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-acl-oper.yang)
* [Cisco-IOS-XE-checkpoint-archive-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-checkpoint-archive-oper.yang)
* [Cisco-IOS-XE-efp-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-efp-oper.yang)
* [Cisco-IOS-XE-ip-sla-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-ip-sla-oper.yang)
* [Cisco-IOS-XE-environment-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-environment-oper.yang)
* [Cisco-IOS-XE-memory-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-memory-oper.yang)
* [Cisco-IOS-XE-process-memory-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-process-memory-oper.yang)
* [Cisco-IOS-XE-process-cpu-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-process-cpu-oper.yang)
* [Cisco-IOS-XE-lldp-oper](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-lldp-oper.yang)
* [ietf-interfaces](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-interfaces.yang)

The filenames from github should give you an idea of what each structure provides oper-data for. Let's take a look at an example from an open model; ietf-interfaces:

```                                 
./ncc.py --host=172.36.170.252 --get-oper -x '/interfaces-state/interface[name="GigabitEthernet0/0"]/oper-status'
```    
NOTE: For more details on the use of ncc, please see [here](https://github.com/CiscoDevNet/ncc)

The data returned will be the operational data defined in the YANG model, for the interface in question. Here are result details:
```
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet0/0</name>
      <oper-status>up</oper-status>
    </interface>
  </interfaces-state>
</data>

```
NOTE: XPATH is being used for a specific query of the oper-status of a single interface.

Finally, the models above represent the beginning of what types of oper-data are enabled by default over a model-driven interface via polled. More oper-data models will be delivered in future releases of software.

## Non-default oper-data

There are 2 types of non-default oper-data. One type provided through an onboard Operational Data Manager (or ODM). Another type is SNMP.

### Operational Data Manager

The Operational Data Manager (or ODM) was initially supported in IOS-XE 16.3 for routers, and in IOS-XE 16.5 for switches. This writeup assumes an IOS-XE 16.5 deployment. ODM represents a collection of parsers that can be optionally enabled to be exposed over NETCONF/RESTCONF.

##### Configuration

Have you ever noticed additional CLI that gets enabled after you enabled NETCONF or RESTCONF? Here is a router example:
```
netconf-yang cisco-odm actions BGP
netconf-yang cisco-odm actions OSPF
netconf-yang cisco-odm actions IPRoute
netconf-yang cisco-odm actions Diffserv
netconf-yang cisco-odm actions FlowMonitor
netconf-yang cisco-odm actions BFDNeighbors
netconf-yang cisco-odm actions BridgeDomain
netconf-yang cisco-odm actions VirtualService
netconf-yang cisco-odm actions EthernetCFMStats
netconf-yang cisco-odm actions MPLSLDPNeighbors
netconf-yang cisco-odm actions PlatformSoftware
netconf-yang cisco-odm actions MPLSStaticBinding
netconf-yang cisco-odm actions MPLSForwardingTable
```

Here is a switch example:
```
etconf-yang cisco-odm actions BGP
netconf-yang cisco-odm actions OSPF
netconf-yang cisco-odm actions IPRoute
netconf-yang cisco-odm actions Diffserv
netconf-yang cisco-odm actions FlowMonitor
netconf-yang cisco-odm actions BFDNeighbors
netconf-yang cisco-odm actions MPLSLDPNeighbors
netconf-yang cisco-odm actions PlatformSoftware
netconf-yang cisco-odm actions MPLSStaticBinding
netconf-yang cisco-odm actions MPLSForwardingTable
```

All these commands are initially inert, and saved to the configuration. The configurations represent oper-data of the following YANG models:
* BGP - [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-bgp-oper.yang)
* OSPF - [ietf-ospf.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-ospf.yang)
* IPRoute - [ietf-routing.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-routing.yang), [ietf-ipv4-unicast-routing.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-ipv4-unicast-routing.yang), [ietf-ipv6-unicast-routing.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-ipv6-unicast-routing.yang)
* Diffserv - [ietf-diffserv-target.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/ietf-diffserv-target.yang)
* FlowMonitor - [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-flow-monitor-oper.yang)
* BFDNeighbors - [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-bfd-oper.yang)
* BridgeDomain -
* VirtualService -
* EthernetCFMStats -
* MPLSLDPNeighbors - [Cisco-IOS-XE-mpls-ldp.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-mpls-ldp.yang)
* PlatformSoftware - [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/Cisco-IOS-XE-platform-software-oper.yang)
* MPLSStaticBinding - [common-mpls-static.yang](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1651/common-mpls-static.yang)
* MPLSForwardingTable -

NOTE: the configuration lines above applies equally to RESTCONF. In other words, the config above is put into a network element automatically once **netconf-yang or restconf** are enabled. To enable oper-data for the models described above, they need to be enabled to be polled. One additional config line is needed:
```
**netconf-yang cisco-odm polling-enable**
```
This enables the components above to have oper-data exposed through polling. ODM polls the components themselves, and answers NETCONF <get> or RESTCONF GET requests on the components behalf. Let's take a look at an example from an open model; ietf-routing:

```                                 
./ncc.py --host=172.36.170.252 --get-oper -x '/routing-state/routing-instance/ribs/rib/routes/route[destination-prefix="0.0.0.0/0"]"
```
The result should be the information in the elements routing table, as defined by the model. Here is an example result:
```
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
    <routing-instance>
      <name>Mgmt-vrf</name>
      <ribs>
        <rib>
          <name>ipv4-default</name>
          <routes>
            <route>
              <destination-prefix>0.0.0.0/0</destination-prefix>
              <route-preference>1</route-preference>
              <metric>0</metric>
              <next-hop>
                <next-hop-address>172.26.170.1</next-hop-address>
              </next-hop>
              <source-protocol>static</source-protocol>
            </route>
          </routes>
        </rib>
      </ribs>
    </routing-instance>
  </routing-state>
</data>
```
NOTE: NOTE: XPATH is being used for a specific query of a single route.

Finally, from a NETCONF point of view, your software should be able to determine the presence of the ODM on the network element through the following from a capabilities exchange:
```
<capability>http://cisco.com/yang/cisco-odm?module=cisco-odm&amp;revision=2017-01-25</capability>
```

Happy coding!
