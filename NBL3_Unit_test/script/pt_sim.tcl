set l_alias [lindex $argv 0]
set l_value [lindex $argv 1]
set l_occ [lindex $argv 2]
ScsDbm::init
puts ${l_alias}
ScsDbm::writeInteger ${l_occ} 1 <alias>${l_alias}:dac.veTable(0,1)
ScsDbm::writeInteger ${l_occ} ${l_value} <alias>${l_alias}:dac.veTable(0,2)
puts <alias>${l_alias}
# ScsDbm::writeInteger OCC 1 <alias>ZXNSYSFEPPSCADA:dciOCS-COM:dac.veTable(0,1)