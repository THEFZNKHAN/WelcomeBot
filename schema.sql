create table if not exists welcome(
    guild_id BIGINT PRIMARY KEY,
    channel_id BIGINT NOT NULL,
    message VARCHAR(255) NOT NULL DEFAULT 'Welcome **{user}** to **{guild}**!'
);
