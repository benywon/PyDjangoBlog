var lr = document.referrer;  //��·
var sf = location.href;      //�ܷ�
var cookieExpireTime = 7 * 24 * 60 * 60;
if (lr != null && lr != '' && lr != 'http://wangpai.2345.cn')
{
	var regTg = /http:\/\/tg\.jifen\.2345\.com/;  //������·�Ǵ�tg.jifen.2345.com������������cookie
    if(regTg.exec(lr)){
    	RC.cset('cookielr', lr, cookieExpireTime);
    }

	if (document.referrer.indexOf('tg.jifen.2345.com') > -1)
	{
		RC.cset('cookielr', lr, cookieExpireTime);		
	}	
}
var showPop = false;

var showUrls = [
    'http://jifen.2345.com/',
    'http://jifen.2345.com/s/jifen/',
    'http://jifen.2345.com/s/lipin/list',
    'http://jifen.2345.com/help/',
    'http://jifen.2345.com/know.php',
    
    'http://wangpai.2345.cn/',
    'http://wangpai.2345.cn/thread.php?fid=12&pid=2569024',
    'http://wangpai.2345.cn/thread.php?fid=12&pid=2488499',
    'http://wangpai.2345.cn/thread.php?fid=12&pid=2513324',
    'http://wangpai.2345.cn/forumdisplay.php?fid=12',
    'http://wangpai.2345.cn/forumdisplay.php?fid=13',
    
    'http://wangpai.2345.cn/thread.php?fid=13&pid=2139380',
    'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=25',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=47',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=20',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=40',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=41',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=53',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=54',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=42',
	'http://wangpai.2345.cn/forumdisplay.php?fid=13&tid=35',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=39',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=57',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=55',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=52',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=51',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=50',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=49',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=38',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=37',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=48',
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=15', 
	'http://wangpai.2345.cn/forumdisplay.php?fid=12&tid=36',	
	'http://wangpai.2345.cn/thread.php?fid=13&pid=2553948'	
];

var requestUrl = location.protocol+'//'+location.hostname + location.pathname + location.search;

for(var i in showUrls) {
	//console.log(showUrls[i]);
	if (showUrls[i] == requestUrl) {
		showPop = true;
		break;
	}
}

var cookielr = RC.cget('cookielr');
if (showPop && cookielr && !IS_LOGIN) {		
	//document.writeln('<script src="http://jifen.2345.com/jifenimg/js/user_num.js" type="text/javascript" />');
	//RC._loadJs('http://jifen.2345.com/jifenimg/js/user_num.js');
	var tg_user_num = 1845024;
	if (jf_user_num)
	{
		tg_user_num = jf_user_num.user_num; 
	}
	
	document.writeln('<link href="css/tg/tg.css" rel="stylesheet" type="text/css" />');
	document.writeln('<div class="tg_pop">');
	document.writeln('  <a class="close" href="javascript:void(0);" onclick="$(\'.tg_pop\').hide();">�ر�</a>');
	document.writeln('  <div class="tg_pop_in">');
	document.writeln('  <div class="counter">'+tg_user_num+'</div>');
	document.writeln('    <fieldset class="tg_form_reg">');
	document.writeln('      <legend>����ע��</legend>');
	document.writeln('      <ul class="tg_reg clearfix">');
	document.writeln('        <li>');
	document.writeln('          <p class="inp_box"><label id="label1" class="like_label" for="username">�û���</label><input id="username" class="inp" type="text" name="username" value="" onblur="checkUser();" onfocus="on_focus(\'1\', \'3-24�����ֻ���ĸ������\');" /></p>');
	document.writeln('          <p id="toptip1">3-24�����ֻ���ĸ������</p>');
	document.writeln('        </li>');
	document.writeln('        <li>');
	document.writeln('          <p class="inp_box"><label id="label2" class="like_label" for="password">����</label><input id="password" class="inp" type="password" name="password" value="" onblur="checkPass();" onfocus="on_focus(\'2\', \'��6-16����ĸ�����ֺͷ������\')" /></p>');
	document.writeln('          <p id="toptip2">��������6-16����ĸ�����ֺͷ������</p>');
	document.writeln('        </li>');
	document.writeln('        <li>');
	document.writeln('          <p class="inp_box"><label id="label3" class="like_label" for="email">����</label><input id="email" class="inp" type="text" name="email" value="" onblur="checkEmail();" onfocus="on_focus(\'3\',\'��������Ч�ĵ�������\')" /></p>');
	document.writeln('          <p id="toptip3">��������Ч�ĵ�������</p>');
	document.writeln('        </li>');
	document.writeln('        <li><a class="btn_reg" href="javascript:void(0);" onclick="checkTgSubmit(); return false;">����ע��</a></li>');
	document.writeln('      </ul>');
	document.writeln('    </fieldset>');
	document.writeln('  </div>');
	document.writeln('</div>');
	
	
	
	document.writeln('<div class="pop" style="display:none; z-index: 99999;" id="r_n_l_w">');
	document.writeln('  <div class="pop_con" style="width:550px">');
	document.writeln('    <div class="tit"><a title="�ر�" class="ico_close_blue" href="javascript:void(0)" onclick="$(\'#r_n_l_w\').hide();"></a>�û���¼</div>');
	document.writeln('    <div class="p20 clearfix">');
	document.writeln('    <span class="ico38 ico_warn2L fleft mr20"></span>');
	document.writeln('    <div class="fleft" style="width:450px">');
	document.writeln('    <p class="p1">�벻Ҫ���ף��������ϸ�ķ����׻��ƣ����׻ᱻ<em class="fred">�����˺�</em>��һ�����ò���Ǯ�ģ�</p>');
	document.writeln('    <p class="p1">��Ʒ�һ�ʱ��Ҫ��֤�ֻ��źͼ�ͥ��ַ��һ������ͨ�����׷�ʽƭǮ�����ǻ��ύ�������ش�����򵱵ط�Ժ��<em class="fred">թƭ��</em>�������ߣ�</p>');
	document.writeln('    <div class="pt10 mt10 fleft">');
	document.writeln('    <div style="float:left; width:50px; margin-top:8px; font-size:14px">��֤��</div>');
	document.writeln('    <div class="fleft">');
	document.writeln('    <div class="inputTxt mr10">');
	document.writeln('	<div class="inner"><input class="noborder" type="text" value="1" style="" id="tgImageCode" name="tgImageCode"></div>');
	document.writeln('	</div>');
	document.writeln('    <img onclick="changeTgImage();" style="cursor:pointer; margin-right:10px" id="tgPic" >');
	document.writeln('    <a href="javascript:void(0);" onclick="changeTgImage();" >�����壬��һ��</a>');
	document.writeln('    <div class="mt10">�����������</div>');
	document.writeln('    <div class="mt15"><a class="pub_btnA_L" href="javascript:void(0)" onclick="checkTgValidate();return false;"><span>ȷ��</span></a></div>');
	document.writeln('    </div>');
	document.writeln('    </div>');
	document.writeln('    </div>');
	document.writeln('    </div>');
	document.writeln('    </div>');
	document.writeln('</div>');	
	document.writeln('<form action="" id="hiddenTgForm" name="hiddenTgForm" method="post">');  		
	document.writeln('</form>');  
}

function checkUser() {
	var username = $("#username").val();
	//username = $.trim(username);
    if (username === '') {
    	show_label("1");
        show_err("����û�������û���","1");
		return false;
    }

	if (strlen(username) < 3 || strlen(username) > 24) {
		show_err("������3��24���ַ�","1");
		return false;
	}
    
    if (/^0/.test(username)) {
        show_err("�û�����һ���ַ�������Ϊ0","1");
		return false;
    }

	if (/[^\u4E00-\u9FA5\w_@\.]/.test(username)) {
		show_err("�����뺺�֣���ĸ�����֣��������ַ","1");
		return false;
	}
	
	var err = 0;
	$.ajax({
		 type: "POST",
		 url: "/api/regCheck.php",
		 async: false,
		 cache: false,
		 data: "type=username&username="+username,
		 success: function(response){
		 	if (response == 1) 
			{
				err = 1;
			} 
			else if (response == 2) 
			{
				err = 2;
			}
			else 
			{
                                err = 0;
                                //����û����������ַ�����Զ���д�����ַ
                                if (/^[_\.0-9a-z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\.)+[a-zA-Z]{2,4}$/.test(username)) {
                                        $("#email").val(username);
                                        checkEmail();
                                }
			}
		 }
	});
	if (err == 1) {
		show_err("���û����ѱ�ע��","1");
		return false;
	} else if (err == 2) {
		show_err("���û�������Υ����","1");
		return false;
	}

	show_right("1");

	return true;
}

function checkPass() {
	var pass = $("#password").val();
	if (pass == "")
	{
		show_label("2");
	}	
	
	if ( pass.length < 6 || pass.length > 16 ) {
		show_err("������6��16���ַ�������","2");
		return false;
	}
	if (pass == $('#username').val()) {
		show_err("���벻�����û���һ��","2");
		return false;
	}
	if (pass == '123456' || pass == '654321' || pass == '111222') {
		show_err("������ڼ򵥣�����������","2");
		return false;
	}
	
	if(check_passwd_strong(pass)){
		show_err("������ʹ��5����ͬ���ַ�","2");
		return false;
	}

	show_right("2");
	return true;
}

function check_passwd_strong(passwd){
	if(passwd.length < 6){return true;}
	var patrn=/^[0-9]{0,7}$/;  
	if (patrn.exec(passwd)){return true;}
	if(get_char_count(passwd) < 5){return true;}
	return false;
	function get_char_count(str){
		var count = 0;
		var uniqueString = '';
		for(var i=0;i<str.length;i++)
		{
			if(uniqueString.indexOf(str[i]) >= 0)
			{
				continue;
			}
			uniqueString += str[i];
		}
		count = uniqueString.length;
		return count;
	}
}

function checkEmail() {
	var email = $("#email").val();
	//email = $.trim(email);
	
	if (email == "") {
		show_label("3");
		show_err('����������',"3");
		return false;
	}
	if (!/^[_\.0-9a-z-]+@([0-9a-zA-Z][0-9a-zA-Z-]+\.)+[a-zA-Z]{2,4}$/.test(email)) {
		show_err('������������ʽ����ȷ',"3");
		return false;
	}

	var err = 0;
    var userName = '';
	$.ajax({
		 type: "POST",
		 url: "/api/regCheck.php",
		 async: false,
		 cache: false,
		 data: "type=email&email="+email,
		 success: function(response){
                        if (response == 1) {
                        	err = 1;
                        } else {
                            err = 0;
                        }
		 }
	});
	if (err == 1) {
		show_err('<a href="http://login.2345.com/get_pw.php" target="_blank">�������ѱ�ע�ᣬ�û���Ϊ'+userName+'��������һ�����</a>',"3");
        return false;
	} else if(err == 2) {
        return false;
    }
	show_right("3");
	return true;
}


function show_label(id){
	$("#label"+id).show();
}

function show_err(str, id){
	$("#toptip"+id).addClass('warning');
	$("#toptip"+id).html(str);
}

function show_right(id){
	$("#toptip"+id).removeClass('warning');
	$("#toptip"+id).html('');
}

function on_focus(id, str) {
	$("#toptip"+id).html(str);
	$("#label"+id).hide();
}

function strlen(str){
    var len = 0;
    for (var i=0; i<str.length; i++) {
        var c = str.charCodeAt(i);
        if ((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)) {
           len++;
        }
        else {
           len+=2;
        }
    }
    return len;
}

function changeTgImage()
{
	var url = '/randCaptcha.php?'+Math.random();
	$('#tgPic').attr({src:url});
}

function need_fill_vc()
{
	changeTgImage();
	var divTop = gTop('r_n_l_w');;
	$('#r_n_l_w').css('top', divTop + 'px');
	var divLeft = gLeft('r_n_l_w');;
	$('#r_n_l_w').css('left', divLeft + 'px');			
	$("#r_n_l_w").show();
	return false;	
}

function checkTgSubmit()
{
	if (!checkUser()) {
		return false;
	}
	if (!checkPass()) {
		return false;
	}	
	if (!checkEmail()) {
		return false;
	}	
	if(!need_fill_vc()){
		return false;
	}
	tg_cc('wangpai_tg_register');
}

function tg_cc(vUrl)
{
	// url���
	var web = "ajax39"; 
	var url = 'http://union2.50bang.org/web/'+web+'?uId2=SPTNPQRLSX&r='+encodeURIComponent(document.location.href)+'&fBL='+screen.width+'*'+screen.height+'&lO='+encodeURIComponent(vUrl); 
	var _dh = document.createElement("script"); 
	_dh.setAttribute("type","text/javascript"); 
	_dh.setAttribute("src",url); 
	document.getElementsByTagName("head")[0].appendChild(_dh); 
	return true; 
}

function checkTgValidate()
{
	var d = new Date();
	var err = 0;//0 ����   1��ȷ
	var imgCode = $("#tgImageCode").val();
	var email = $("#email").val();
	var password = $("#password").val();
	var username = $("#username").val();	
	var postData = {
			cmd:'login',
			remember: 1,
			type:'tgReg',
			username:username,
			password:password,
			repass:password,
			email:email,
			imgCode:imgCode,
			cookielr:cookielr,
			jstime:d.getTime()
	};	
	
   	$.ajax({
		url: "/api/regCheck.php",
		type: "POST",
		data: postData
	}).done(function(data){	
		obj = eval("("+data+")");	
		if (obj.resCode != '200.0')
		{
			alert(obj.resMsg);
			return false;			
		}	

		var action = 'http://login.2345.com/login.php';
		var loginData = {
				cmd:'login',
				username:username,
				password:MD5(password),
				forward:'http://jifen.2345.com/signup/link.php',
				jstime:d.getTime()
		};
		$('#r_n_l_w').hide();
		buildTgForm(action, loginData);		
	});   		
	
	return false;
}

function buildTgForm(action, postData)
{
	RC.$('hiddenTgForm').action = action;			
	
	for(var el in postData){
		var newElement = document.createElement("input");
	    newElement.setAttribute("name", el);
	    newElement.setAttribute("type", "hidden");
	    newElement.setAttribute("value", postData[el]);
	    RC.$('hiddenTgForm').appendChild(newElement);
	}
	
	RC.$('hiddenTgForm').submit();
}

function gTop(objQuery)
{
	var scrollTop = $(window).scrollTop();
	var top = scrollTop + ($(window).height() - $('#' + objQuery).height()) / 2;
	return top;
}

function gLeft(objQuery)
{
	left = (($(window).width() - $('#' + objQuery).width()) / 2);
	return left;
}

jQuery(window).scroll(function(){
	var divTop = gTop('r_n_l_w');;
	$('#r_n_l_w').css('top', divTop + 'px');
	var divLeft = gLeft('r_n_l_w');;
	$('#r_n_l_w').css('left', divLeft + 'px');	
});


function GetHttpRequest()
{
    if ( window.XMLHttpRequest ) // Gecko
        return new XMLHttpRequest() ;
    else if ( window.ActiveXObject ) // IE
        return new ActiveXObject("MsXml2.XmlHttp") ;
}
function AjaxPage(sId, url){
    var oXmlHttp = GetHttpRequest() ;
    oXmlHttp.OnReadyStateChange = function() 
    {
        if ( oXmlHttp.readyState == 4 )
        {
            if ( oXmlHttp.status == 200 || oXmlHttp.status == 304 )
            {
                IncludeJS( sId, url, oXmlHttp.responseText );
            }
        }
    }
    oXmlHttp.open('GET', url, true);
    oXmlHttp.send(null);
}
function IncludeJS(sId, fileUrl, source)
{
    if ( ( source != null ) && ( !document.getElementById( sId ) ) ){
        var oHead = document.getElementsByTagName('HEAD').item(0);
        var oScript = document.createElement( "script" );
        oScript.language = "javascript";
        oScript.type = "text/javascript";
        oScript.id = sId;
        oScript.defer = true;
        oScript.text = source;
        oHead.appendChild( oScript );
    }
}