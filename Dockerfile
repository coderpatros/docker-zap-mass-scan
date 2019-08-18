FROM owasp/zap2docker-stable

USER zap
COPY mass-* /zap/
RUN mkdir /zap/wrk


USER root
RUN chown zap /zap/mass-*

USER zap
ENTRYPOINT [ "/zap/mass-scan.sh" ]