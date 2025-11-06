FROM gcr.io/cloud-builders/gcloud

ENV HELM_VERSION=v3.13.0

RUN apt-get update && \
    apt-get install -y wget curl && \
    wget https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz && \
    tar -zxvf helm-${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    rm -rf helm-${HELM_VERSION}-linux-amd64.tar.gz linux-amd64 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify installation
RUN helm version

ENTRYPOINT ["helm"]