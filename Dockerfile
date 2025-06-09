FROM node:18

WORKDIR /app
COPY dist-final ./dist
RUN npm install -g serve

EXPOSE 4173
CMD ["serve", "-s", "dist-final", "-l", "4173", "--single"]
