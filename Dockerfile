FROM python:3.6
WORKDIR /root

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY siteroot /root/siteroot
WORKDIR /root/siteroot
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
