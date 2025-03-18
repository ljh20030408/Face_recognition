package com.zjnu.facebackend.controller;

import com.zjnu.facebackend.service.RecordsService;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/records")
@CrossOrigin
public class RecordsController {
    @Resource
    RecordsService recordsService;

    @PostMapping("/getRecordsPage")
    public R getRecordsPage(@RequestBody Page page){
        return recordsService.getRecordsPage(page);
    }



}
