set l_station [lindex $argv 0]
set l_sys [lindex $argv 1]
set l_occ [lindex $argv 2]
ScsDbm::init
ScsDbm::writeInteger ${l_occ} 1 <alias>${l_station}SYSFEP${l_sys}:dciOCS-COM:dac.veTable(0,1)
ScsDbm::writeInteger ${l_occ} 1 <alias>${l_station}SYSFEP${l_sys}:dciOCS-COM:dac.veTable(0,2)
# ScsDbm::writeInteger OCC 1 <alias>ZXNSYSFEPPSCADA:dciOCS-COM:dac.veTable(0,1)