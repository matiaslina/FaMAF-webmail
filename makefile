BINARY=/usr/bin/webmail

install:
	@echo "Copiando archivos en ${BINARY}"
	@cp webmail.py ${BINARY}
	@echo "Haciendo ejecutable el programa"
	@chmod +x ${BINARY}

uninstall:
	@echo "Removiendo los archivos necesarios..."
	@rm ${BINARY}
