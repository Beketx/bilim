server {
    listen ${LISTEN_PORT};
    server_name ${IP};

    location /static {
        alias /vol/static;
    }

    location / {
        proxy_pass http://${APP_HOST}:${APP_PORT};
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_connect_timeout       800;
        proxy_send_timeout          800;
        proxy_read_timeout          800;
        send_timeout                800;
    }
}
