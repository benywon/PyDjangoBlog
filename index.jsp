<%@page import="main.ResultShow.ResultDisplay"%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="main.*" %>
<jsp:useBean id="docomo" scope="application" class="main.DealQuestion.DealQuestion" />
<jsp:useBean id="result" scope="application" class="main.ResultShow.ResultDisplay" />
<jsp:useBean id="myfile" scope="application" class="main.Filebases" />

<%
    String path = request.getContextPath();

    String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
    String resourcePath = getServletContext().getRealPath("/") ;
    String ip="";
    if(request.getHeader("x-forwarded-for") == null)
    {
        ip= request.getRemoteAddr();
    }
    else
    {
        ip=request.getHeader("x-forwarded-for");
    }

    System.out.println("ip:\t"+ip);
    String qa_text = request.getParameter("qatext");
    String question = "请输入旅游相关的问题\t 比如海淀区的公园 水立方的营业时间 附近有假山的公园等等 ";
    System.out.println("原始类型"+result.showType);
	result.showType=0;
    if(qa_text!=null)
    {
		
        if(!qa_text.equals(""))
        {
            question=qa_text;
			
            System.out.println(question);			
            String add="";
            try{
                result =docomo.dealthisquesion(question);
                if(result.showType == result.OnlyString)
                {
                    add=result.result;
                }
                else
                {
                    add=result.resultnumber+"";
                }
                myfile.Write2File("类型：" + result.origentype + " 问题：" + question + "\t" + add + "\t" + result.gettime() + "\tIP地址:\t" + ip + "<br>", "C:\\Users\\beny\\apache-tomcat-8.0.26\\webapps\\docomo\\1.html",true);
                result.show();
            }catch(Exception e)
            {
                e.printStackTrace();
                result.setShowType(result.Warning);
                result.show();
            }
        }
        else//输入东西
        {
            System.out.println();
            result.setShowType(result.NoQueryWarning);
            result.show();
        }


    }
    if(!docomo.isload)
    {
        System.out.println("开始初始化我们的内容");
        System.out.println(resourcePath);
        docomo.InitiationAllResource(resourcePath);
    }


%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <base href="<%=basePath%>">
    <javascript src="/docomo/js-css/jquery/jquery-1.7.2.min.js"></javascript>
    <javascript src="/docomo/js-css/bootstrap/js/bootstrap.js"></javascript>
    <link href="/docomo/js-css/bootstrap/css/bootstrap.min.css" type="text/css" rel="stylesheet" />


    <!--<link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="/static/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet">
    <script src="/static/jquery/jquery-1.7.2.min.js"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script> -->
    <title>美景任我选</title>
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->
</head>

<body>
<div class = "container">
    <h2>美景查询演示系统</h2>
    <br />
    <br />
    <form name="form" action="" method="get" class="form-inline">
        <input type="text" style="height:30px; width:607px"   placeholder="<%=question%>" name="qatext" value="">
        <input type="submit" class="btn" value="搜索" />
    </form>

        <% if (result.showType == result.OnlyString)  {%>
    <table class="table">
        <tr>
            <td ><%= result.result %></td>
        </tr>

    </table>
        <% }
 else if(result.showType == result.ShowDetail){ %>

    <table class="table table-responsive">
        <tr>
            <th>名称</th><th>位置</th><th>类型</th><th>人均价格</th><th>电话</th><th>城市</th><th>图片</th><th>距离</th>
        </tr>
        <%
            if(result.detailLists!=null)
            {
                for(ResultDisplay.Detail detail:result.detailLists){ %>
        <tr>
            <td><%= detail.name %></td>
            <td><%= detail.position %></td>
            <td><%= detail.type %></td>
            <td><%= detail.ave_price %></td>
            <td><%= detail.telephone %></td>
            <td><%= detail.city %></td>
            <td><img src="<%=detail.pic_url%>" /></td>
            <td><%= detail.distance %></td>
        </tr>
        <%}
        }%>
    </table>
        <% }
else if(result.showType == result.Sentiment){ %>
    <table class="table table-responsive">
        <tr>
            <th>名称</th><th>位置</th><th>类型</th><th>人均价格</th><th>电话</th><th>城市</th><th>图片</th><th>距离</th><th>得分</th><th>情感打分</th><th>点评</th>
        </tr>
        <%
            if(result.detailLists!=null)
            {
                for(ResultDisplay.Detail detail:result.detailLists){ %>
        <tr>
            <td><%= detail.name %></td>
            <td><%= detail.position %></td>
            <td><%= detail.type %></td>
            <td><%= detail.ave_price %></td>
            <td><%= detail.telephone %></td>
            <td><%= detail.city %></td>
            <td><img src="<%=detail.pic_url%>" /></td>
            <td><%= detail.distance %></td>
            <td><%= detail.score %></td>
            <%if(detail.aspectname.length()>0){ %>
            <td><B><%= detail.aspectname %> </B><br>得分：<B><%= detail.aspectscore %></B></td>
            <%}else{ %>
            <td>无</td>
            <%} %>
            <td><%= detail.snippet %></td>
        </tr>
        <%}
        }%>
    </table>
        <% }
	else if(result.showType == result.Warning||result.showType == result.NoQueryWarning){//这是错误的  需要返回错误结果
%>
    <table>
        <tr>
            <td style="color:red;"><b><%= result.result %></b></td>
        </tr>
        <tr>
            <td>错误类型<%=result.showType%></td>
        </tr>

    </table>
        <%}
	else if(result.showType == result.OnlySpot){//可以查的spot
%>
    <table>
        <tr>
            <td><b>名称：</b><a href="<%=result.onlyone.url%>" target="_blank"><%= result.onlyone.name %></a></td>
        </tr>

        <tr>
            <td><b>位置：</b><%= result.onlyone.addr %></td>
        </tr>
        <tr>
            <td><b>价格：</b><%= result.onlyone.ticket %></td>
        </tr>
        <tr>
            <td><b>简介：</b><%= result.onlyone.abstractstr %></td>
        </tr>
        <tr>
            <td><b>星级：</b><%= result.onlyone.star%>星</td>
        </tr>
        <tr>
            <td><b>电话：</b><%= result.onlyone.telephone %></td>
        </tr>
        <tr>
            <td><b>营业时间：</b><%= result.onlyone.shophour %></td>
        </tr>
        <tr>
            <td><b>介绍：</b><%= result.onlyone.description %></td>
        </tr>
    </table>
        <%} else if(result.showType == result.GetQInfo){//这是错误的  需要返回错误结果
%>
    <table>
        <tr>
            <td ><a href="1.html" target="_blank">我们的查询信息</a>></td>
        </tr>

    </table>
        <%} %>
</body>
</html>

