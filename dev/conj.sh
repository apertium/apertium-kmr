echo -n "" > /tmp/v
for i in `cat test-words.txt | sed 's/\t/,/g'`; do 
	#echo $i | cut -f2 -d',' | hfst-proc ../kur.automorf.hfst | sed 's/$/\t/g' | cut -f2- | sh ~/scripts/remove-newline.sh >> /tmp/v
	echo $i | cut -f2 -d',' | hfst-proc ../kur.automorf.hfst  >> /tmp/v

done

paste test-words.txt /tmp/v
