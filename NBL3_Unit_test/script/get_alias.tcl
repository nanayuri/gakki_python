set l_alias [lindex $argv 0]
ScsDbm::init
set fp [open "get_alias.txt" w]
puts $fp [::ScsDbm::getChildrenAliases OCC <alias>${l_alias}]
close $fp