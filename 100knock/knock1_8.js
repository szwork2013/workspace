/* Write JavaScript here */
function q0(){
    var moji ="stressed";
	document.writeln(moji);
	for(i=moji.length;i>=0;i--){
		document.write(moji.charAt(i));
	}
	document.write("<BR>");
}


function q1(){
	moji ="パタトクカシーー";
	document.writeln(moji);
	moji2=moji.charAt(1)+moji.charAt(3)+moji.charAt(5)+moji.charAt(7);
	document.write(moji2);
	document.write("<BR>");
}

function q2(){
	moji1 ="パトカー";
	moji2="タクシー";
	moji3="";
	for(i=0;i<moji1.length;i++){
		moji3=moji3.concat(moji1.charAt(i));
		moji3=moji3.concat(moji2.charAt(i));
	}
	document.writeln(moji3);
	document.write("<BR>");
}

function q3(){
	moji ="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
	array=moji.split(" ");
	for(i=0;i<array.length;i++){
		//余計な句点は消去
		array[i]=array[i].replace(",","");array[i]=array[i].replace(".","");
		document.writeln(array[i].length+" "+array[i]);
	}
	writeline();
}
//Shift+Enterで改行?</BR>でなにも実行できなくなった。
function q4(){
	//変数は後から他人がみても分かる名前でつける
	var elementList=new Object();
	moji="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
	array=moji.split(" ");
	for(i=0;i<array.length;i++){
		//余計な句点は消去
		array[i]=array[i].replace(",","");array[i]=array[i].replace(".","");
		//writeline(i+":"+array[i]);
		switch (i+1){
			case 1:
			case 5:
			case 6:
			case 7:
			case 8:
			case 9:
			case 15:
			case 16:
			case 19:
				elementList[array[i].charAt(0)]=i;
				break;
			default:
				elementList[array[i].substring(0,2)]=i;
				break;
		}
	}
	for (var key in elementList) {
		
　　		writeline(key+":"+elementList[key] );
	}
	writeline();
}
function q5(str,n){
	arrayWord=str.split(" ");
	//文字単位に分割するときはこう
	arrayChar=str.split("");
	writeline(arrayWord);
	writeline(arrayChar);
	var wordBigram=new Array();
	var charBigram=new Array();
	writeline("・WordBigram");
    for (i = 0; i < arrayWord.length - 1; i++) {
        writeline(wordBigram[i] = arrayWord[i] + " " + arrayWord[i + 1]);
    }
    writeline("・CharBigram");
    for (i = 0; i < arrayChar.length - 1; i++) {
        writeline(charBigram[i] = arrayChar[i] + " " + arrayChar[i + 1]);
    }
    writeline("");
    writeline("");
}

function q6() {
    arrayX = "paraparaparadise".split("");
    arrayY = "paragraph".split("");
    X = new Array();
    Y = new Array();
    writeline("・X");
    for (i = 0; i < arrayX.length - 1; i++) {
        X[i] = arrayX[i] + arrayX[i + 1];
    }
    writeline(X);
    writeline("・Y");
    for (i = 0; i < arrayY.length - 1; i++) {
        Y[i] = arrayY[i] + arrayY[i + 1];
    }
    writeline(Y);
    writeline("積集合<BR>" + delDuplication(union(X, Y)));
    writeline("和集合<BR>" + delDuplication(intersection(X, Y)));
    writeline("差集合 X-Y<BR>" + difference(X, Y));
    writeline("差集合 Y-X<BR>" + difference(Y, X));
    writeline("se is " + include("se", X) + " in X.");
    writeline("se is " + include("se", Y) + " in Y.");
    writeline("");

}

function q7(x, y, z) {
    result = x + "時の" + y + "は" + z;
    return result;
}

function q8(str) {
  for(i=0;i<str.length;i++){
    var c=str.charAt(i);
    if(SmallCheck(c)){
  		write(c);
    }else{
      write(cipher(c));
    }
  }
}


//文字を暗号化する

function cipher(str) {
  var c=219-str.charCodeAt(0);
 	string=String.fromCharCode(c);
	return string;
}
/*---------------------------------------------
*				ユーザ関数群
-----------------------------------------------*/
//配列の重複要素を削除
function delDuplication(array) {
    result = array.filter(function(x, i, self) {
        return self.indexOf(x) == i;
    });
    return result;
}

//lodashの使い方がわからないので以下に自作
function include(item, target) {
    for (var i = 0, len = target.length; i < len; i++) {
        if (item == target[i]) {
            return true;
        }
    }
    return false;
}
//積集合
function union(arrayA, arrayB) {
    var result = arrayA.concat();
    for (var i = 0, len = arrayB.length; i < len; i++) {
        if (!include(arrayB[i], result)) {
            result.push(arrayB[i]);
        }
    }
    return result;
}
//和集合
function intersection(arrayA, arrayB) {
    var result = [];
    for (var i = 0, len = arrayB.length; i < len; i++) {
        if (include(arrayB[i], arrayA)) {
            result.push(arrayB[i]);
        }
    }
    return result;
}
//差集合
function difference(arrayA, arrayB) {
    var result = [];
    for (var i = 0, len = arrayA.length; i < len; i++) {
        if (!include(arrayA[i], arrayB)) {
            result.push(arrayA[i]);
        }
    }
    return result;
}

//小文字かチェック
function SmallCheck(char) {
  if (char.match(/[a-z]/g)){
    return true;
  }
}
    //<BR>で改行して出力

function writeline(str) {
        document.write(str);
        document.write("<BR>");
}

function write(str) {
        document.write(str);
}

