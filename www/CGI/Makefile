CC=gcc
AFLAGS=-Wall -g  
OBJS=login.cgi configshow.cgi setconfig.cgi
run:$(OBJS)

$(OBJS):%.cgi:%.c
	$(CC) $(AFLAGS) $< cgic.c -o $@
.PHONY:clean
clean:
	rm *.cgi

