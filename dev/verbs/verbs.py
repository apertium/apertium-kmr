import sys;

# afirandin; TD; afirîn; afirand; ; di ; bi ; ne ; na ; 

configs = {'a': {'$C1': 'kir/__vblex_tv',
		'$C2': 'dik/e__vblex_tv',
		'$C3': 'bik/e__vblex_tv',
		'$C4': 'nekir/__vblex_tv',
		'$C5': 'nak/e__vblex_tv',
		'$C6': 'nek/e__vblex_tv'}, 
	   'b': {'$C1': 'kir/__vblex_tv',
		'$C2': 'dişo/__vblex_tv',
		'$C3': 'bişo/__vblex_tv',
		'$C4': 'nekir/__vblex_tv',
		'$C5': 'naşo/__vblex_tv',
		'$C6': 'neşo/__vblex_tv'},
	   'c': {'$C1': 'axaft/__vblex_iv',
		'$C2': 'diaxiv/e__vblex_iv',
		'$C3': 'biaxiv/e__vblex_iv',
		'$C4': 'neaxaft/__vblex_iv',
		'$C5': 'naaxiv/e__vblex_iv',
		'$C6': 'neaxiv/e__vblex_iv'}};

v_tv_prefix = """
     <!-- $INFI; $PREF; $PAST; $PRES -->
    <e lm="$INFI"><p><l>$PREF$PAST</l><r>$INFI</r></p><par n="$C1"/></e>
    <e lm="$INFI"><p><l>$PREF$AIND$PRES</l><r>$INFI</r></p><par n="$C2"/></e>
    <e lm="$INFI"><p><l>$PREF$PRES</l><r>$INFI</r></p><par n="$C3"/></e>
    <e lm="$INFI"><p><l>$PREF$NSUB$PAST</l><r>$INFI</r></p><par n="$C4"/></e>
    <e lm="$INFI"><p><l>$PREF$NIND$PRES</l><r>$INFI</r></p><par n="$C5"/></e>
    <e lm="$INFI"><p><l>$PREF$NSUB$PRES</l><r>$INFI</r></p><par n="$C6"/></e>
""" ;

v_iv_basic = """     
    <!-- $INFI; ; $PAST; $PRES -->
    <e lm="$INFI"><p><l>$PAST</l><r>$INFI</r></p><par n="$C1"/></e>
    <e lm="$INFI"><p><l>$AIND$PRES</l><r>$INFI</r></p><par n="$C2"/></e>
    <e lm="$INFI"><p><l>$ASUB$PRES</l><r>$INFI</r></p><par n="$C3"/></e>
    <e lm="$INFI"><p><l>$NSUB$PAST</l><r>$INFI</r></p><par n="$C4"/></e>
    <e lm="$INFI"><p><l>$NIND$PRES</l><r>$INFI</r></p><par n="$C5"/></e>
    <e lm="$INFI"><p><l>$NSUB$PRES</l><r>$INFI</r></p><par n="$C6"/></e>
""" ;


v_tv_basic = """     
    <!-- $INFI; ; $PAST; $PRES -->
    <e lm="$INFI"><p><l>$PAST</l><r>$INFI</r></p><par n="$C1"/></e>
    <e lm="$INFI"><p><l>$AIND$PRES</l><r>$INFI</r></p><par n="$C2"/></e>
    <e lm="$INFI"><p><l>$ASUB$PRES</l><r>$INFI</r></p><par n="$C3"/></e>
    <e lm="$INFI"><p><l>$NSUB$PAST</l><r>$INFI</r></p><par n="$C4"/></e>
    <e lm="$INFI"><p><l>$NIND$PRES</l><r>$INFI</r></p><par n="$C5"/></e>
    <e lm="$INFI"><p><l>$NSUB$PRES</l><r>$INFI</r></p><par n="$C6"/></e>
""" ;

def get_template(t, c): #{
	global configs;
	conf = configs[c];
	out = t;
	for i in conf: #{
		out = out.replace(i, conf[i]);
	#}	
	return out;
#}

for line in open('verbs.txt').readlines(): #{
	if line[0] == '#':
		continue;
	(inf, tran, pres, past, pref, aind, asub, nind, nsub, glos, config) = line.strip().split(';');
	entry = '';	
	if tran.strip() == 'tv'and pref.strip() == '': #{
		entry = get_template(v_tv_basic, config.strip()) ;
		entry = entry.replace('$INFI', inf.strip());
		entry = entry.replace('$PAST', past.strip());
		entry = entry.replace('$PRES', pres.strip());
		entry = entry.replace('$AIND', aind.strip());
		entry = entry.replace('$ASUB', asub.strip());
		entry = entry.replace('$NIND', nind.strip());
		entry = entry.replace('$NSUB', nsub.strip());
	elif tran.strip() == 'iv'and pref.strip() == '': #{
		entry = get_template(v_iv_basic, config.strip()) ;
		entry = entry.replace('$INFI', inf.strip());
		entry = entry.replace('$PAST', past.strip());
		entry = entry.replace('$PRES', pres.strip());
		entry = entry.replace('$AIND', aind.strip());
		entry = entry.replace('$ASUB', asub.strip());
		entry = entry.replace('$NIND', nind.strip());
		entry = entry.replace('$NSUB', nsub.strip());
	elif tran.strip() == 'tv'and pref.strip() != '': #{
		entry = get_template(v_tv_prefix, config.strip()) ;
		entry = entry.replace('$INFI', inf.strip());
		entry = entry.replace('$PREF', pref.strip());
		entry = entry.replace('$PAST', past.strip());
		entry = entry.replace('$PRES', pres.strip());
		entry = entry.replace('$AIND', aind.strip());
		entry = entry.replace('$ASUB', asub.strip());
		entry = entry.replace('$NIND', nind.strip());
		entry = entry.replace('$NSUB', nsub.strip());
	#}

	if entry != '':#{
		sys.stdout.write(entry);
	#}
#}
