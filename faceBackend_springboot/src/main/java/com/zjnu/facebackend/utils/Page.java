package com.zjnu.facebackend.utils;

import lombok.Data;

@Data
public class Page {
    //页数据条数
    private Integer pageSize;
    //当时页
    private Integer currentPage;
}
