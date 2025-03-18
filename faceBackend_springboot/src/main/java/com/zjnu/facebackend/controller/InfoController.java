package com.zjnu.facebackend.controller;

import com.zjnu.facebackend.pojo.Info;
import com.zjnu.facebackend.service.InfoService;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@CrossOrigin
@RequestMapping("/info")
public class InfoController {
    @Resource
    InfoService infoService;

    @PostMapping("/getAll")
    public R getAll(@RequestBody Page page){
        return infoService.getAll(page);
    }

    @GetMapping("/deleteById")
    public R deleteById(Long id){
        return infoService.deleteById(id);
    }
}
