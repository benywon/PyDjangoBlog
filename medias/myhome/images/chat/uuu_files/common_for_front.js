/**
 * @author rc-201
 */
var RC = {
    _domain : window.location.host,

    init:function(){
        addEvent(RC.$('nav_top'),"mouseover",
            function(){
                RC.$("whitebg_1").style.display = "";
                RC.$("whitebg_2").style.display = "";
				RC.$("whitebg_3").style.display = "";
            });
        addEvent(RC.$('nav_top'),"mouseout",
            function(){
                RC.$("whitebg_1").style.display = "none";
                RC.$("whitebg_2").style.display = "none";
				RC.$("whitebg_3").style.display = "none";
            });
        addEvent(RC.$('select_d'),"mouseover",
            function(){
                RC.$("bbs_site").style.display = "";
                RC.$("forum_iframe").style.display = "block";
            });
        addEvent(RC.$('select_d'),"mouseout",
            function(){
                RC.$("bbs_site").style.display = "none";
                RC.$("forum_iframe").style.display = "none";
            });

			var domain = document.domain; 
	        var url = window.location.pathname;        
        	if(RC.$("search_text")){
				addEvent(RC.$('search_text'),"click",
					function(){
						if(RC.$('search_text').value == "版块搜索"|| RC.$('search_text').value == "帖子搜索" || RC.$('search_text').value == '请输入搜索内容'){
							RC.$('search_text').value = "";
							RC.$('search_text').style.color = 'black';
						}
					});
			}


        if(url != '/search.php'){
			if(RC.$("search_text")){
            addEvent(RC.$('search_text'),"blur",
                function(){
                    if(RC.$('search_text').value == ""){            //搜索框文字search_text
                        if(domain == 'wangpai.2345.cn' || domain == 'shoujibbs.2345.cn')
                        {
                        	RC.$('search_text').value = '请输入搜索内容';
                        }else
                        {
                        	if(url == '/' || url == '/index.php'){
                                RC.$('search_text').value = '版块搜索';
                            }else{
                                RC.$('search_text').value = '帖子搜索';
                            }                        	
                        }	
                    	
                        RC.$('search_text').style.color = '#999';
                    }
                });
            
	            if(domain == 'wangpai.2345.cn' || domain == 'shoujibbs.2345.cn')
	            {
	            	RC.$('search_text').value = '请输入搜索内容';
	            }else
	            {
	                //搜索框文字search_text
	                if(url == '/' || url == '/index.php'){
	                    RC.$('search_text').value = '版块搜索';
	                }else{
	                    RC.$('search_text').value = '帖子搜索';
	                }	            	
	            }	
			}
        }

    },
    $ : function(_id) {
        return document.getElementById(_id);
    },
    _names:function(_name){
        return document.getElementsByName(_name);
    },
    _c : function(_tag) {
        return document.createElement(_tag);
    },
    _html : function(_id, _con) {
        if(_con == undefined) {
            return RC.$(_id).innerHTML;
        } else {
            RC.$(_id).innerHTML = _con;
        }
    },
    _class:function(_id,_className){
        if(_className == undefined){
            return RC.$(_id).className;
        }else{
            RC.$(_id).className = _className;
        }
    },
    _loadJs : function(_url) {
        var b = RC._c("script");
        b.setAttribute("type", "text/javascript");
        b.setAttribute("src", _url);
        document.getElementsByTagName("head")[0].appendChild(b);
        return true;
    },
    cset: function(a, b) {
        var c = [],
        _para = {};
        for (var d = 0, _len = arguments.length; d < _len; d++) {
            c[d] = arguments[d];
        };
        _para.exps = typeof(c[2]) != "undefined" ? Math.ceil(c[2] / (3600 * 24)) : undefined;
        _para.name = c[0];
        _para.val = c[1];
        _para.path = c[3];
        _para.domain = c[4];
        _para.secure = c[5];
        RC.util.cookie.set(_para);
        return false;
    },
    cget: function(a) {
        return RC.util.cookie.get(a);
    },

    cdel: function(a) {
        RC.util.cookie.del(a);
    },
    checkAll: function(e, itemName){
        var obj = RC._names(itemName);
        for (var i=0; i<obj.length; i++)
            obj[i].checked = e.checked;
    },
    GetPageScroll:function(i){
        var x, y;
        if(window.pageYOffset){
            // all except IE
            y = window.pageYOffset;
            x = window.pageXOffset;
        } else if(document.documentElement && document.documentElement.scrollTop){
            // IE 6 Strict
            y = document.documentElement.scrollTop;
            x = document.documentElement.scrollLeft;
        } else if(document.body) {
            // all other IE
            y = document.body.scrollTop;
            x = document.body.scrollLeft;
        }
        return i=='x'?x:y;
    },
    showDiv: function(nDiv){
        //alert();
        var w, h, ow, oh;
        var dbg = RC.$("divBg");

        w = document.body.scrollWidth;
        if(document.body.scrollHeight < window.screen.height)
        h = window.screen.height+50;
        else
        h =  document.body.scrollHeight+50;
        dbg.style.width = w + 'px';
        dbg.style.height = h + 'px';
        dbg.style.display = "block";

        var onDiv = RC.$(nDiv);
        var pw = parseInt(onDiv.style.width.substr(0, (onDiv.style.width.length - 2))); //ff
        if (isNaN(pw)) {
            pw = 0;
        }
        onDiv.style.left = (w - pw) / 2 + "px";
        onDiv.style.top = RC.GetPageScroll('y')+250 + "px";//RC.GetPageScroll('y') 获取滚动条当前的滚动位置 确定图层显示的位置
        onDiv.style.display = "";
        onDiv.disabled = false;
        //		scroll(0,0);
        var s = arguments.length;
        if (s == 2)
            RC.$(arguments[1]).focus();
        return false;
    },
    //隐藏div
    hideDiv: function(nDiv){
        var s = arguments.length;
        //不关闭背景
        if (s != 2)
            RC.$("divBg").style.display = "none";
        var onDiv = RC.$(nDiv);
        onDiv.style.display = "none";
        onDiv.disabled = true;
        return true;
    },
    search_text: function(){
        if(RC.$('search_text').value == '' || RC.$('search_text').value == '版块搜索' || RC.$('search_text').value == '帖子搜索' || RC.$('search_text').value == '请输入搜索内容')
            RC.$('search_text').value = '';
      
        if (RC.$('search_text').value == '')
        {
        	alert('对不起,搜索关键字不能为空');
        	return false;
        }	
        
        var e = RC.$('search_post_form');
        var url = window.location.pathname;
        var domain = document.domain; 
        
        if(domain == 'wangpai.2345.cn' || domain == 'shoujibbs.2345.cn')
        {
        	if(url == '/search.php'){
                e.action = '/search.php?action=my';
            }else{
                e.action = '/search.php';
            }        	        
        }else
        {
            if(url == '/' || url == '/index.php'){
                e.action = "/index.php";
            }else if(url == '/search.php'){
                e.action = '/search.php?action=my';
            }else{
                e.action = '/search.php';
            }        	
        }	
        
        //e.submit();
    },
    search_text2: function(){
        if(RC.$('search_text').value == '' || RC.$('search_text').value == '版块搜索' || RC.$('search_text').value == '帖子搜索' || RC.$('search_text').value == '请输入搜索内容')
            RC.$('search_text').value = '';
      
        if (RC.$('search_text').value == '')
        {
        	alert('对不起,搜索关键字不能为空');
        	return false;
        }	
        
        var e = RC.$('search_post_form');
        var url = window.location.pathname;
        var domain = document.domain; 
        
        if(domain == 'wangpai.2345.cn' || domain =='shoujibbs.2345.cn')
        {
        	if(url == '/search.php'){
                e.action = '/search.php?action=my';
            }else{
                e.action = '/search.php';
            }        	        
        }else
        {
            if(url == '/' || url == '/index.php'){
                e.action = "/index.php";
            }else if(url == '/search.php'){
                e.action = '/search.php?action=my';
            }else{
                e.action = '/search.php';
            }        	
        }	

        return true;
        //e.submit();
    },   
    
    replaceAll: function(str, sptr, sptr1) {
    	while (str.indexOf(sptr) >= 0) {
    		str = str.replace(sptr, sptr1);
    	}
    	return str;
    },
    util : {
        cookie : {
            _exps: 180,
            get : function(a) {
                var b = document.cookie.split("; ");
                for(var c = 0; c < b.length; c++) {
                    tmp = b[c].split("=");
                    if(tmp[0] == a) {
                        try {
                            return decodeURIComponent(tmp[1]);
                        } catch(e) {
                            return unescape(tmp[1]);
                        }
                    }
                }
                return null
            },
            set : function(a) {
                var b = new Date();
                var c = a.name, _val = a.val, _exps = typeof (a.exps) != "undefined" ? a.exps : this._exps, _domain = a.domain || this._domain, _path = a.path || "/", _secure = a.secure || this._secure;
                b.setDate(b.getDate() + _exps);
                var d = c + "=" + escape(_val) + ( _exps ? ";expires=" + b.toUTCString() : "") + ( _path ? ";path=" + _path : "") + ( _domain ? ";domain=" + _domain : "") + ( _secure ? ";secure=" : "");
                document.cookie = d
            },
            del : function(a) {
                if(String.prototype.toLowerCase.apply( typeof (a)) == "string") {
                    _name = a;
                    a = {
                        name : _name,
                        val : ""
                    }
                }
                a.exps = -1;
                a.secure = "";
                this.set(a)
            }
        }
    },
    verification : {
        //验证
        _vTitle:function(_id,_messageID){
            if(RC.$(_id).value == "" || RC.$(_id).value.trim() == ''){
                RC._html(_messageID,'<span style="color:red">请输入标题</span>');
                RC.$(_id).focus();
                return false;
            }else if(!(/^[\u4E00-\u9FA5\w\W_ ~]+$/.test(RC.$(_id).value))){
                RC._html(_messageID,'<span style="color:red">标题格式不正确</span>')
                RC.$(_id).focus();
                return false;
            }else if(RC.$(_id).value.length > 80){
                RC._html(_messageID,'<span style="color:red">标题长度不能大于80字符</span>')
                RC.$(_id).focus();
                return false;
            }else{
                RC._html(_messageID,'');
                return true;
            }
        },
        _vContent:function(_id,_messageID){
            if(RC.$(_id).value == "" || RC.$(_id).value.trim() == ''){
                RC._html(_messageID,'<span style="color:red">请输入内容</span>')
                RC.$(_id).focus();
                return false;
            }else if(RC.$(_id).value.length > 10000){
                RC._html(_messageID,'<span style="color:red">内容长度不能大于10000字符</span>')
                RC.$(_id).focus();
                return false;
            }else{
                RC._html(_messageID,'不超过10000字符');
                return true;
            }
        },
        _vInfo:function(_messageID){
            var qq = RC.$('qq').value;
            var mobile = RC.$('mobile').value;
            var other = RC.$('other').value;

            if(qq == "" && mobile == "" && other == ""){
                RC._html(_messageID,'<span style="color:red">请输入联系方式</span>')
                RC.$('qq').focus();
                return false;
            }else if(qq != "" && !(/^\d{5,}$/.test(qq))){
                RC._html(_messageID,'<span style="color:red">请输入正确的联系方式</span>')
                RC.$('qq').focus();
                return false;
            }else{
                RC._html(_messageID,'');
                return true;
            }
        },
        _vCode:function(_id,_messageID){
            if(RC.$(_id).value == ""){
                RC._html(_messageID,'<span style="color:red">请输入验证码</span>')
                RC.$(_id).focus();
                return false;
            }else{
                RC._html(_messageID,'')
                return true;
            }
        }
    }
};

var ready_ = false;
document.onready = function() {
    if (ready_) {
        return;
    }
    ready_ = true;
    RC.init();
};
function bindReady() {
    if (document.addEventListener) {
        document.addEventListener("DOMContentLoaded",
            function() {
                document.removeEventListener("DOMContentLoaded", arguments.callee, false);
                document.onready();
            },
            false)
    } else if (document.attachEvent) {
        document.attachEvent("onreadystatechange",
            function() {
                if (document.readyState === "complete") {
                    document.detachEvent("onreadystatechange", arguments.callee);
                    document.onready();
                }
            });
        if (document.documentElement.doScroll && window == window.top)(function() {
            if (ready_) return;
            try {
                document.documentElement.doScroll("left");
            } catch(e) {
                setTimeout(arguments.callee, 0);
                return;
            }
            document.onready();
        })()
    }
}

bindReady();

function addEvent(a, b, c) {
    if (!a) return false;
    if (!c.$$guid) c.$$guid = addEvent.guid++;
    if (!a || !a.events) a.events = {};
    var d = a.events[b];
    if (!d) {
        d = a.events[b] = {};
        if (a["on" + b]) {
            d[0] = a["on" + b];
        }
    }
    d[c.$$guid] = c;
    a["on" + b] = handleEvent;
}
addEvent.guid = 1;
function removeEvent(a, b, c) {
    if (a.events && a.events[b]) {
        delete a.events[b][c.$$guid];
    };
}
function handleEvent(a) {
    a = a || window.event;
    var b = this.events[a.type];
    for (var i in b) {
        this.$$handleEvent = b[i];
        this.$$handleEvent(a);
    }
}
function search_enter(evt){
	var currKey=0;
	currKey=evt.keyCode||evt.which||evt.charCode; 
	if(currKey == 13)
	{
		RC.search_text();
	}
}

function suijishu(_id){
	RC.$(_id).src = "check_code.php?"+Math.random();
}

/**
 * JS 去掉文本中的空格
 */
String.prototype.trim = function() {
    return this.replace(/(^\s*)|(\s*$)/g, "");
};


function searchSubmitEnter(evt){
	 var currKey=0; 
	 currKey=evt.keyCode||evt.which||evt.charCode;
	 if(currKey == 13)
	 {
		var flg = RC.search_text2();
		var e = RC.$('search_post_form');
		if (flg)
		{
			e.submit();
		}
		return false;	
	 }
	 else
	 {
		 return true;
	 } 	 	 
}

function searchSubmitCheck()
{
	var flg = RC.search_text2();
	var e = RC.$('search_post_form');
	if (flg)
	{
		e.submit();
	}	  
	return false;
}

function forbidSubmit(obj, clsName, butVal)
{
	jq('#' + obj).attr("class", clsName); 
	//jq('#' + obj).val(butVal);
	jq('#' + obj).html('<span>' + butVal + '</span>');	
	jq('#' + obj).attr("disabled","true"); 
	jq('#' + obj).removeAttr('onclick'); 
	jq('#' + obj).click( function() {
		return false;
	});	
}

function wangpaiforbidSubmit(obj, clsName, butVal)
{
	$('#' + obj).attr("class", clsName); 
	$('#' + obj).html('<span>' + butVal + '</span>');	
	$('#' + obj).attr("disabled","true"); 	
	$('#' + obj).removeAttr('onclick'); 
	$('#' + obj).click( function() {
		return false;
	});		
}

function getContentLength(content)
{
	var stripHtmlContent = content.replace(/<\/?.+?>/g,"");
	var stripHtmlContent = stripHtmlContent.replace(/&nbsp;/g,"");
	var stripHtmlContent = stripHtmlContent.replace(/\s/g,"");
	var totalLength = stripHtmlContent.length;

	
	var imgPattern = /<img((?!kindedit\/plugins\/emoticons)[^>])+>/ig;
	var imgLengh = 0;
    while(imgPattern.exec(content))
    {
    	imgLengh++;
    }
	totalLength = totalLength + imgLengh * 15;

	return totalLength; 
}

var bbsContentMaxLength = 10000;

var uploadFilesMaxSize = 5;
var currentUploadFileNum = 0;
var uploadFileDefaultImg = 'http://' + document.domain + '/js/kindedit/themes/default/placeholder.gif';

function delUploadifyPic(myJquery)
{
	myJquery(".uploadPic .del").each(function(){
		myJquery(this).click( function() {
			delPicLi(myJquery, this);
		})
	}); 
}

function delPicLi(myJquery, ele)
{
	
	if (currentUploadFileNum > 0)
	{
		currentUploadFileNum--;
	}
	
	if (currentUploadFileNum == 0)
	{
		myJquery('.ke-dialog-footer [type="button"]').each(function(){
			var btnVal = myJquery(ele).attr('value');
			if (btnVal == '图片上传')
			{
				myJquery(ele).attr('disabled', true);
				myJquery(ele).attr('style', 'color:#999;cursor:default;');
			}						
		});
	}	
	
	if (currentUploadFileNum < uploadFilesMaxSize)
	{
		//myJquery('#tipUploadMsg').html('按住ctrl可选择多张图片，每次最多上传5张图片');
	}
	
	var fileImg = myJquery(ele).parent().siblings("img");
	myJquery.ajax({
		url: "/ajax.php",
		type: "POST",
		data: {act:'delPic',fileSrc:fileImg.attr('fileSrc'),fileExt:fileImg.attr('fileExt')}
	}).done(function(data){	
		obj = eval("("+data+")");			
	});

	myJquery(ele).parent().parent().remove();
	myJquery(".uploadPic ul").append('<li><img src="'+uploadFileDefaultImg+'" width="70px" height="70px" /><div class="operate" style="display:none;"><span class="del" onclick="delPicLi(myJquery, this);"></span></div>');

}

function initUploadifyPic(myJquery)
{
	uploadFilesMaxSize = 5;
	currentUploadFileNum = 0;
	var domainName = document.domain;
	var user_name  = '';
	if (utname)
	{
		user_name = utname; 
	}	
	var currentTime = new Date().getTime();
	if (RC.cget('I'))
	{
		var userDetail = RC.cget('I');
	}
	else
	{
		var userDetail = RC.cget('user_info');
	}

	if (!userDetail)
	{
		userDetail = ''; //修正当user_info是null时， uploadify控件js报错的问题
	}
	
	myJquery('#file_upload').uploadify({
		//'uploadLimit' : 5, 
		'formData'   : {'user_name' : user_name, 'user_info' : userDetail, 'domainName' : domainName},
		'buttonText' : '添加图片',
		'buttonClass' : 'pub_btnB_S',
		'fileTypeExts'  : '*.gif; *.jpg; *.png; *.jpeg; *.bmp',
		'fileTypeDesc'  : 'Image Files',
		'fileSizeLimit' : '2048KB',
		'width'  : 65,
		'height'  : 23,
		'swf'      : '/js/uploadify/uploadify.swf',
		'uploader' : 'http://' + domainName + '/uploadify.php?' + currentTime,
    	'onUploadSuccess' : function(file, data, response) {
    		myJquery('.ke-dialog-footer input[type="button"]').removeAttr('disabled');
    		myJquery('.ke-dialog-footer input[type="button"]').removeAttr('style');
			currentUploadFileNum = currentUploadFileNum + 1;
			//alert(currentUploadFileNum + '==' + uploadFilesMaxSize);
			if (currentUploadFileNum == uploadFilesMaxSize)
			{
				//myJquery('#tipUploadMsg').html('<font class="fred">每次最多上传5张图片</font>');
				//alert('cancel');
				uploadifyOperate('cancel');
				uploadifyOperate('destroy');
				initUploadifyPic(myJquery);
			}	

    		var res = myJquery.parseJSON(data);
			var showFlg = false;
			if (res.code == 1)
			{
				//alert(res.msg);
				var fileExt = '';
				var fileSrc = '';
				myJquery(".uploadPic img").each(function(i){ 
					//alert(jq(this).attr('src'));						 (
					fileExt = myJquery(this).attr('fileExt');
					fileSrc = myJquery(this).attr('src');
					//alert('==' + fileExt + "==");
					//if (fileExt == '' || fileExt == 'undefined')
					if (fileSrc == uploadFileDefaultImg)
					{
						myJquery(this).attr('fileExt', res.fileExt);
						myJquery(this).attr('fileSrc', res.sourceImage);
						myJquery(this).attr('src', 'http://' + domainName + res.sourceImage);
						myJquery(this).siblings(".operate").show(); 	
						//myJquery(this).siblings(".operate").children(".del").bind("click", function(){delPicLi(myJquery, this);}); 

						//alert('http://' + document.domain + res.sourceImage);
						return false;
					}
												
				}); 						
			}
			else
			{
				if (res.msg != '')
				{
					alert(res.msg);
				}else
				{
					alert('文件上传失败!');
				}	
			}
    	},  	
		'onSelect' : function(file){
		}	
	});
}

function uploadifyOperate(opt)
{
	myJquery('#file_upload').uploadify(opt);
}

function bbs_cc(vUrl)
{
	// url组合
	var host = window.location.host;
	if (host.indexOf("shoujibbs") == -1)
	{
		var web = "ajax39"; 
	}
	else
	{
		var web = "ajax109"; 
	}
	var url = 'http://union2.50bang.org/web/'+web+'?uId2=SPTNPQRLSX&r='+encodeURIComponent(document.location.href)+'&fBL='+screen.width+'*'+screen.height+'&lO='+encodeURIComponent(vUrl); 
	var _dh = document.createElement("script"); 
	_dh.setAttribute("type","text/javascript"); 
	_dh.setAttribute("src",url); 
	document.getElementsByTagName("head")[0].appendChild(_dh); 
	return true; 
}
