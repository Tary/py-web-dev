<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
		<title>{{title}}</title>
    </head>

    <body >
	    <center>
		    <table>
				<tr>
					<td width="120">
						<h3>编辑器发布</h3>
						<li><a href="publish/SkillEditor">技能编辑器</a></li><br/>
						<li><a href="publish/ParticleEditor">粒子编辑器</a></li><br/>
						<li><a href="publish/SceneEditor">场景编辑器</a></li>
					</td>
					<td width="120">
						<h3>编辑器下载</h3>
						<li><a href="/download/SkillEditor.exe">技能编辑器</a></li><br/>
						<li><a href="/download/ParticleEditor.exe">粒子编辑器</a></li><br/>
						<li><a href="/download/SceneEditor.exe">场景编辑器</a></li>
					</td>
				</tr>
				<tr>
					<form action="/upload" method="post" enctype="multipart/form-data">
						<input type="file" name="data"/>
						<input value="提交" type="submit" />
					</form>
				</tr>
		    </table>
			
	    </center>
    </body>
</html>
