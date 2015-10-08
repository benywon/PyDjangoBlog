$("#myForm_username").die().live("keydown", function(event){        
    if(event.keyCode==13){       
    	check('myForm');     //调用登陆方法;      
    }        
});

$("#myForm_pwd").die().live("keydown", function(event){        
    if(event.keyCode==13){       
    	check('myForm');      //调用登陆方法;     copy 
    }        
});

$("#loginForm_pImgCode").die().live("keydown", function(event){        
    if(event.keyCode==13){       
    	subOpenLoginDiv();     //调用登陆方法;     
    }        
});

function check(formName)
{	
	var username = RC.$(formName + '_username'  ).value;
	var pwd      = RC.$(formName + '_pwd'  ).value;
	var password = MD5(pwd);
	var forward  =  self.location.href;
	var pImgCode = '';
	if (formName != 'myForm')
	{
		//提交后需要隐藏登录层， 显示消息层
		RC.$('loginPop').style.display = 'none';
		pImgCode = RC.$(formName + '_pImgCode'  ).value;
	}
	
	var postData = {cmd:'login', username:username,password:password, pImgCode: pImgCode, forward: forward, remember: 1};
	//用户验证
	$.post('/wangpaiLogin.php?'+Math.random(), 
			postData, 
		function(data){
			var result   = eval('[' + data + ']');
			var codeNum  = result[0].codeNum; 
			var errCount = RC.$('errorPoperrCount').value ; 
			if(codeNum == 100)
			{
				var locationUrl = result[0].locationUrl;
				buildForm(locationUrl, postData);
			}else if(codeNum == 7)
			{
				var locationUrl = result[0].locationUrl;
				window.location.href = locationUrl;
			}else if(codeNum ==6 || codeNum == 7 || codeNum == 8)
			{
				if(codeNum == 6)
				{
					postData.id = result[0].id;	
				}
				var locationUrl = result[0].locationUrl;
				buildForm(locationUrl, postData);
				
			}else if(codeNum == 105){
				if(errCount > 0){
					openErrPop(3, formName);return false;
				}else{
					openLoginDiv(formName);
					RC.$('errorPoperrCount').value = 1;
				}
			}else{
				openErrPop(codeNum, formName);																							
			}	

			return false;
		}
	);	
	return false;			
}

function ccimage()
{
	var imgSrc = 'http://jifen.2345.com/randCaptcha.php?'+Math.random();	
	$('#pic').attr('src',imgSrc);
	$("input[name='pImgCode']").val('');
}

function openErrPop(codeNum, formName)
{
	var scrollWidth = document.documentElement.scrollWidth || document.body.scrollWidth;
	var scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;			
	$('#divBg').css('height', scrollHeight);
       
	RC.$('divBg').style.display = '';
	RC.$('errorPop').style.display = '';
	if(codeNum == 1){
		RC.$('errorPopMsg').innerHTML = '请输入2345帐号!';	
	}else if(codeNum == 2){
		RC.$('errorPopMsg').innerHTML = '请先输入密码!';	
	}else if(codeNum == 3){
		RC.$('errorPopMsg').innerHTML = '验证码输入错误，请重新输入!';
		$("input[name='pImgCode']").val('');
	}else if(codeNum == 4){
		RC.$('errorPopMsg').innerHTML = '请重新输入验证码!';	
	}else if(codeNum == 5){
		RC.$('errorPopMsg').innerHTML = '2345帐号或密码错误!';	
	}else if(codeNum == 101){
		RC.$('errorPopMsg').innerHTML = '未知错误!';	
	}
	RC.$('errorPopformName').value = formName;
}

function sureErrPop()
{
	var codeNum  = RC.$('errorPopcodeNum').value;
	var formName = RC.$('errorPopformName').value;
			
	closeErrPop();
	if(formName == 'loginForm') openLoginPop();	
		
	setErrFocus(codeNum, formName);
}
		
function closeErrPop(){
	RC.$('divBg').style.display = 'none';
	RC.$('errorPop').style.display = 'none';	
}
		
function setErrFocus(codeNum, formName)
{
	if(codeNum == 1 || codeNum == 5 || codeNum == 101){			
		if(RC.$(formName + '_username'  )){
			$('#' + formName + '_username').focus();
		}
	}else if(codeNum == 2){			
		if(RC.$(formName + '_pwd'  )){
			$('#' + formName + '_pwd').focus();
		}
	}else if(codeNum == 3 || codeNum == 4){	
		if(RC.$(formName + '_pImgCode'  )){				
			RC.$(formName + '_pImgCode'  ).focus();	
		}
	}						
}

function openLoginPop()
{
	var left = ((jQuery(window).width() - jQuery("#loginPop").width()) / 2) + 'px';	 
	jQuery("#loginPop").css('left',  left);		
	var scrollTop = document.documentElement.scrollTop + document.body.scrollTop;
	RC.$("loginPop").style.top = (scrollTop + 100) + "px";
	RC.$('loginPop').style.display = '';	
}		

function closeLoginPop()
{
	RC.$('loginPop').style.display = 'none';
	RC.$('errorPoperrCount').value = 0;
}

function buildForm(action, postData)
{
	RC.$('hiddenForm').action = action;			
	for(var el in postData){
		var newElement = document.createElement("input");
	    newElement.setAttribute("name", el);
	    newElement.setAttribute("type", "hidden");
	    newElement.setAttribute("value", postData[el]);
	    RC.$('hiddenForm').appendChild(newElement);
	}
	
	RC.$('hiddenForm').submit();
}

function openLoginDiv(formName)
{
	ccimage();
	var username = RC.$(formName + '_username'  ).value;
	var pwd      = RC.$(formName + '_pwd'  ).value;
	RC.$('loginForm_username').value = username;
	RC.$('loginForm_pwd').value = pwd;	
	$('#loginForm_pImgCode').focus();
	openLoginPop();
	return false;	
}

function subOpenLoginDiv()
{
	var pwd =$("#loginForm_pwd").val();
	$('#loginForm_password').val(MD5(pwd));
	RC.$('errorPoperrCount').value = 0;
	var forward  =  self.location.href;
	$('#loginForm_forward').val(forward);
	$('#loginForm').submit();
}