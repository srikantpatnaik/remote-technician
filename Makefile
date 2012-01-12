# Makefile for remote-technician
.PHONY= clean all

all:
	python server.py
clean:
	@echo "cleaning up..."
	-rm -rvf *~ .*~ \#* *.o
distclean:
	$(MAKE) clean


