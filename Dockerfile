
#Base image
FROM python:3.10-slim

#Set working directory
WORKDIR /app

#Copy requirements file first
COPY requirements.txt .


#Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

#Copy files
COPY . .

#Expose Jupyter port
EXPOSE 8888


#Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
