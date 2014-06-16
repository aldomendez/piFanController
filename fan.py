#! /usr/bin/env python

import subprocess as sb

sb.call('/opt/vc/bin/vcgencmd measure_temp | egrep "[0-9.]{4,}" -o', shell=True)



