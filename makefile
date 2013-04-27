BINARY=/usr/bin/webmail
PIXBUF=/usr/share/pixmaps/


install:
	@echo "Copiando archivos en ${BINARY}"
	cp webmail.py ${BINARY}
	mkdir -p ${PIXBUF}
	cp pixmaps/famaf-webmail.png ${PIXBUF}
	@echo "Haciendo ejecutable el programa"
	@chmod +x ${BINARY}

uninstall:
	@echo "Removiendo los archivos necesarios..."
	rm ${BINARY}
	rm -f ${PIXBUF}
