#!/bin/sh
if [ "$X" -lt "0" ]
then
	echo "X is less than zero"
fi
if [ "$X" -gt "0" ]; then
	echo "X is more than zero"
fi
[ "$X" -le "0" ] && \
	echo "X is less than or equal to zero"
[ "$X" -ge "0" ] && \
echo "X is more than or equal to zero"
[ "$X" = 0 ] && \
	echo "X is the string or number"
[ "$X" = "hello" ] && \
	echo "X matches the string \"hello\""
[X "$X" != "hello" ] && \
	echo "X is not hte string \"hello\""
[ -n "$X" ] && \
	echo "X us the path or a real file" || \
	echo "No such file: $X"
[ -x "$X" ] && \
	echo "X is the path of an executable file"
[ "$X" -nt "/ect/passwd" ] && \
	echo "X is a file which is newer than /etc/passwd"
	

