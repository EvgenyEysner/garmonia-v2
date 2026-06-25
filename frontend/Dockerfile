FROM node:24-slim AS build

WORKDIR /frontend

ARG VITE_API_BASE_URL=https://schoenheitsecke-oldenburg.de
ARG VITE_STUDIO_LOCATION=53.1428031,8.2226412
ARG VITE_GA4_ID=

ENV VITE_API_BASE_URL=$VITE_API_BASE_URL \
    VITE_STUDIO_LOCATION=$VITE_STUDIO_LOCATION \
    VITE_GA4_ID=$VITE_GA4_ID

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
