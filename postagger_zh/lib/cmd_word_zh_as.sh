CLASS=com.aliasi.demo.demos.ChineseWordsDemo
ARGS="Academia_Sinica,/models/words-zh-as.CompiledSpellChecker"

CMD=com.aliasi.demo.framework.DemoCommand

CP=$1:$1/lib/lingpipe-demos.jar:$1/lib/lingpipe-4.1.0.jar:$1/lib/nekohtml-1.9.14.jar:$1/lib/xercesImpl-2.9.1.jar:$1/lib/xml-apis-2.9.1.jar

export LANG=en_US.UTF-8
java -cp $CP $CMD -demoConstructor=$CLASS -demoConstructorArgs=$ARGS $2 $3 $4 $5 $6 $7 $8 $9
