server {
    listen ${LISTEN_PORT};
    server_name ${IP};

    location /static {
        alias /vol/static;
    }

    location / {
        proxy_pass http://${APP_HOST}:${APP_PORT};
        proxy_redirect off;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
