import pytest


# pytest.main(["--html=Outputs/Reports/report.html","--junitxml=Outputs/Reports/report.xml","-m",
#             "joinclassSuccess","--reruns","1"])
pytest.main(["--html=Outputs/Reports/report.html","--junitxml=Outputs/Reports/report.xml","-m",
            "joinclassSuccess","--reruns","1","--alluredir=Outputs\Allures"])

#报错的话，可以删除命令之后再重新安装
# pytest.main(['-s', '-q', '--alluredir', './report/html'])
#一定一定记住代码不能敲错，--junitxml=Outputs/Reports/report.xml这里的后面是.xml
