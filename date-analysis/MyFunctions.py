def InsertTr(ofh, tag, s=0, *argv):
    tab = "\t"
    eol = "\n"
    if s != 0:
        colspan = " colspan=" + str(s)
        tags = "<" + tag + colspan + ">"
    else:
        tags = "<" + tag + " >"
    tage = "</" + tag + "> "
    ofh.write("<tr>\n")
    ofh.write(tab)
    for data in argv:
        ofh.write(tags + data + tage)
    ofh.write(eol)
    ofh.write("</tr>\n")
