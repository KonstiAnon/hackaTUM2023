FROM node:18-alpine as build

RUN corepack enable

WORKDIR /app

COPY package.json .
COPY pnpm-lock.yaml .

RUN pnpm install

COPY . .

RUN pnpm run build

FROM nginx:alpine as run

COPY --from=build /app/dist /usr/share/nginx/html