#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from simple_template import SimpleTemplate

m_header='''
<?xml version="1.0" encoding="Shift_JIS"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head profile="http://purl.org/net/ns/metaprof">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <title>お問い合わせ | 高知市　六泉寺歯科</title>
    <meta name="keywords" content="高知市,六泉寺歯科,歯医者,お問い合わせ" />
    <meta name="description" content="当サイト「六泉寺歯科～Rokusenji Dental Clinic～」のお問い合わせになります" />
    <meta http-equiv="pragma" content="no-cache" />
    <link rel="index" href="./" title="六泉寺歯科" />
    <link rel="prev" href="../clinic.html" title="医院紹介" />
    <link rel="next" href="../general.html" title="一般歯科・小児歯科" />
    <link rel="stylesheet" type="text/css" href="../css/styles.css" />
    <link rev="made" href="mailto&#58;web&#64;freesale&#46;co&#46;jp" />
    <script type="text/javascript" src="../js/jquery.js"></script>
    <script type="text/javascript" src="../js/jquery.textarearesizer.js"></script>
    <script type="text/javascript" src="../js/interface.js"></script>
    <script type="text/javascript" src="../js/externallink.js"></script>
    <script type="text/javascript" src="../js/rollover.js"></script>
    <script type="text/javascript" src="../js/jquery-sweetlink.js"></script>

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.16/vue.js">

    <script type="text/javascript" src="http://www.google.com/jsapi?key="></script>
    <script type="text/javascript" src="../js/gmap.js?auto"></script>
    <script>
        $(document).ready(function(){
            if( /Android|iPhone|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
                var img = $('#sp_map').html();
                $('#sp_map').html('<a href="http://maps.google.com/maps?q=33.539301, 133.541625">'+img+'</a>');
            }
        });
    </script>
    <script type="text/javascript">
        $(function(){
            $('textarea.resizable:not(.processed)').TextAreaResizer();
        });
    </script>
    <script type="text/javascript" src="http://www.google-analytics.com/ga.js"></script>
    <!-- Google Analytics start -->
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', "UA-3981132-1"]);
        _gaq.push(['_trackPageview']);

        (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
    </script>
    <!-- Google Analytics end -->
</head>

<body id="contact">
    <div id="wrapper">
        <div id="header">
            <h1>高知市の六泉寺歯科 | 一般歯科・審美治療(ホワイトニングなど)・インプラントに関する情報を掲載しております。</h1>
            <div id="top"><a href="./" accesskey="1"><img src="../images/h1.jpg" alt="高知市　六泉寺歯科"></a></div>
            <div class="section">
                <div class="toptxt">スマートフォンでタップすると発信画面に切り替わります。</div>
                <p class="tel"><a href="tel:0888336406" class="sweetlink sweetlink-icon-tel" onClick="jQuery.sweetlink(function(){ _gaq.push(['_trackEvent', 'phone_call', 'header', 'bnr_img', , true]); })"><img src="../images/header-tel.jpg" width="156" height="79" alt="お問い合わせはコチラまで　088-833-6406" /></a></p>
                <ul id="header_nav">
                    <li id="nav01"><a href="./" title="トップページへ">TOP</a></li>
                    <li id="nav02"><a href="../sitemap.html" title="サイトマップのページへ">SITEMAP</a></li>
                </ul>
            </div>
            <p id="catch-copy"><img src="../images/catch-copy.jpg" width="300" height="80" alt="口元は健康の第一の入り口です。" /></p>
        </div>
        <div id="main" class="clearfix">
            <div id="content">
'''

m_footer='''
            </div>
            <div id="nav">
                <div id="left_nav">Contents</div>
                <dl>
                    <dt id="cat01">医院紹介</dt>
                    <dd id="nav03"><a href="../dr.html">院長紹介</a></dd>
                    <dd id="nav04"><a href="../clinic.html">医院紹介</a></dd>
                    <dd id="nav05"><a href="../contact.html">お問い合わせ</a></dd>
                    <dt id="cat02">診療内容</dt>
                    <dd id="nav06"><a href="../general.html">一般歯科・小児歯科</a></dd>
                    <dd id="nav07"><a href="../aesthe.html">審美歯科</a></dd>
                    <dd id="nav08"><a href="../implant.html">インプラント</a></dd>
                    <dd id="nav09"><a href="../ortho.html">矯正歯科</a></dd>
                    <dd id="nav10"><a href="../prevent.html">予防歯科</a></dd>
                    <dd id="nav11"><a href="../sitemap.html">サイトマップ</a></dd>
                </dl>
                <p><a href="http://www.shika-town.com/f00000879/"><img src="../images/shika-town.png" width="180" height="70" alt="歯科タウン　六泉寺が掲載されています" /></a></p>
                <p><a href="contact.html"><img src="../images/ban-contact.png" width="180" height="60" alt="カウンセリング・ご相談　問い合わせ受付はこちら" /></a></p>
                <p><a href="https://www.shika-town.com/reservation.php?pre=search&amp;cl=39004"><img src="../images/ban-reserve.png" width="180" height="60" alt="診療予約受付　WEBで24時間受け付けています" /></a></p>
                <p class="ban_sjcd"><a href="http://www.shikoku-sjcd.com/">SJCD</a></p>
            </div>
            <div id="footer">
                <p class="alpha"> <a href="tel:0888336406" class="sweetlink sweetlink-icon-tel" onClick="jQuery.sweetlink(function(){ _gaq.push(['_trackEvent', 'phone_call', 'footer', 'bnr_img', , true]); })"><img src="../images/footer-tel.jpg" width="202" height="80" alt="お問い合わせはコチラまで 088-833-6406" /></a> </p>
                <div class="beta">
                    <dl>
                        <dd><a href="./">トップページ</a> | </dd>
                        <dd><a href="..\/clinic.html">医院紹介</a> | </dd>
                        <dd><a href="..\/contact.html">お問い合わせ</a></dd>
                    </dl>
                    <address>
                        Copyright &copy; 六泉寺歯科クリニック All Rights Reserved.
                    </address>
                    <p class="maps" id="add02"><img src="../images/maps.jpg" width="200" height="70" alt="地図アプリを起動する" /></p>
                    <script type="text/javascript">
                        if(navigator.userAgent.indexOf("iPhone") > 0) {
                            document.write('<p class="maps"><a href="http://maps.google.com/maps?q=33.539301, 133.541625"><img src="../images\/maps.jpg" alt="地図アプリを起動する 高知市六泉寺町15-13" width="200" height="70" /><\/a><\/p>');
                            $("#add02").remove();
                        }
                        else if(navigator.userAgent.indexOf("iPad") > 0) {
                            document.write('<p class="maps"><a href="http://maps.google.com/maps?q=33.539301, 133.541625"><img src="../images\/maps.jpg" alt="地図アプリを起動する 佐高知市六泉寺町15-13" width="200" height="70" /><\/a><\/p>');
                            $("#add02").remove();
                        }
                        else if(navigator.userAgent.indexOf("Android") > 0) {
                            document.write('<p class="maps"><a href="http://maps.google.com/maps?q=33.539301, 133.541625"><img src="../images\/maps.jpg" alt="地図アプリを起動する 高知市六泉寺町15-13" width="200" height="70" /><\/a><\/p>');
                            $("#add02").remove();
                        }
                    </script>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''
def header():
	#return SimpleTemplate(m_header.decode("utf-8").encode("utf-8")).render()
	#return (SimpleTemplate(m_header).render())
	return m_header

def footer():
	#return SimpleTemplate(m_footer.decode("utf-8").encode("utf-8")).render()
	print m_footer

