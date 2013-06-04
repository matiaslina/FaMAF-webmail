BINARY=/usr/bin/webmail
APP_FOLDER=/usr/share/famaf-webmail
PIXBUF=/usr/share/pixmaps/famaf-webmail.png
MANPAGE=/usr/share/man/man1/webmail.1.gz

install:
	mkdir -p ${PIXBUF}
	cp pixmaps/famaf-webmail.png ${PIXBUF}
	mkdir -p ${APP_FOLDER}
	cp webmail.py ${APP_FOLDER}
	cp config.py ${APP_FOLDER}
	cp webmail ${BINARY}
	cp man/webmail.1.gz ${MANPAGE}
	@echo "Haciendo ejecutable el programa"
	@chmod +x ${BINARY}
	


uninstall:
	@echo "Removiendo los archivos necesarios..."
	rm ${BINARY}
	rm ${PIXBUF}
	rm -rf ${APP_FOLDER}
	rm ${MANPAGE}
