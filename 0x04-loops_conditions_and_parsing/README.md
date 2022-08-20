<!DOCTYPE html>

<h1 class="gap">0x04. Loops, conditions and parsing</h1>

<div class="panel-body">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/BC2neyc5GcI" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220623%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220623T171337Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=9de05cc1b3bb25ec10e63ba65944d9b8cca52f6be383350fd2181c8cba3fd7ce" alt="" style=""></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/XnVjFM8a1W4RfRu4TCPY-g" title="The <code>for</code> loop&quot; target=“_blank”>The <code>for</code> loop</a> </li>
<li><a href=" rltoken="" tkpmmkxbw4dgkxdkt51fza"="" 6mzdeyytpw9r1k0hbkfubq"="" zoh3mqvvhyo_itinhksv6q"="" target="_blank">Loops sample</a> </li>
<li><a href="/rltoken/IM0Gv6VPzwAmqzlJxETZkw" title="Variable assignment and arithmetic" target="_blank">Variable assignment and arithmetic</a> </li>
<li><a href="/rltoken/K3E6xI9-goDM-93vsjCpPA" title="Comparison operators" target="_blank">Comparison operators</a> </li>
<li><a href="/rltoken/0OZLLDT28KrRZdid-l6hwg" title="File test operators" target="_blank">File test operators</a> </li>
<li><a href="/rltoken/Dyrnap2UC-LrzrmCOJRx8A" title="Make your scripts portable" target="_blank">Make your scripts portable</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>env</code></li>
<li><code>cut</code></li>
<li><code>for</code></li>
<li><code>while</code></li>
<li><code>until</code></li>
<li><code>if</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/AVktLDpuzzD92vXnfuqeWg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.7.0</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>More Info</h2>

<h3>Shellcheck</h3>

<p><a href="/rltoken/E7Pr2zeM3cdY5-C0HKwtbw" title="Shellcheck" target="_blank">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. <code>Shellcheck</code> is your friend! <strong>All your Bash scripts must pass <code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>

<p><code>Shellcheck</code> is available on the school’s computers. If you want to use it on your own computer, here is how to <a href="/rltoken/SOX0HZTMgzHbcxrvU1X4hw" title="install it" target="_blank">install it</a>.</p>

<p>Examples:</p>

<p>Not passing <code>Shellcheck</code>:<br>
<br>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png" alt="" style=""></p>

<p>Passing <code>Shellcheck</code>:<br>
<br>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png" alt="" style=""></p>

<p>For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code <code>SC2034</code>, you can browse <a href="/rltoken/1SeRQAUtYIpfXXIQeD1PFQ" title="https://github.com/koalaman/shellcheck/wiki/SC2034" target="_blank">https://github.com/koalaman/shellcheck/wiki/SC2034</a>.</p>

  </div>
