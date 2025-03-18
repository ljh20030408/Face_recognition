package com.zjnu.facebackend.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.zjnu.facebackend.mapper.InfoMapper;
import com.zjnu.facebackend.pojo.Info;
import com.zjnu.facebackend.service.InfoService;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;


/**
* @author April in lie
* @description 针对表【info】的数据库操作Service实现
* @createDate 2023-04-12 16:29:05
*/
@Service
public class InfoServiceImpl implements InfoService {

    @Resource
    InfoMapper infoMapper;

    @Override
    public R getAll(Page page) {
        Integer pageSize = page.getPageSize();
        Integer currentPage = page.getCurrentPage();
        PageHelper.startPage(currentPage,pageSize);
        List<Info> info = infoMapper.getAll();
        PageInfo<Info> pageInfo = new PageInfo<>(info);
        return new R().success(pageInfo);
    }

    @Override
    public R deleteById(Long id) {
        R r = new R<>();
        Boolean aBoolean = infoMapper.deleteById(id);
        if (aBoolean){
            return r.success("删除成功");
        }
        r.setMsg("删除失败");
        return r;
    }
}




