# Overview

This interface layer handles the communication between the [NameNode][]s
in an HA deployment of the Apache Hadoop cluster.


# Usage

## Peers

The NameNode uses this interface internally to manage its peer relations.

This interface layer will set the following states, as appropriate:

  * `{relation_name}.joined` The NameNode is HA.  It can get information
    about the cluster with the following methods:
      * `nodes()`  The list (max 2) of NameNode host names, including this one
      * `hosts_map()`  The hosts mapping of all other NameNodes


# Contact Information

- <bigdata@lists.ubuntu.com>


# Hadoop

- [Apache Hadoop](http://hadoop.apache.org/) home page
- [Apache Hadoop bug trackers](http://hadoop.apache.org/issue_tracking.html)
- [Apache Hadoop mailing lists](http://hadoop.apache.org/mailing_lists.html)
- [Apache Hadoop Juju Charm](http://jujucharms.com/?text=hadoop)


[NameNode]: https://github.com/juju-solutions/layer-apache-hadoop-namenode/
