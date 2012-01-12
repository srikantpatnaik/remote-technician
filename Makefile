# Makefile for remote-technician
webapp=webapp
.PHONY= clean all

all:
	python server.py
clean:
	@echo "cleaning up..."
	-rm -rvf *~ .*~ \#* *.o
distclean:
	$(MAKE) clean
	cd $(webapp) ; make


