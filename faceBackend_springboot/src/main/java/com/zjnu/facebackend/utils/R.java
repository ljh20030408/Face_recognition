package com.zjnu.facebackend.utils;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class R<T> {

    //返回信息码
    private String code;
    //返回信息
    private String msg;
    //返回数据
    T data;

    //成功，只返回成功码和信息
    public R<T> success(){
        R<T> R=new R<>();
        R.setCode(ResultCode.SUCCESS.code);
        R.setMsg(ResultCode.SUCCESS.msg);
        return R;
    }

    //成功，返回成功码、信息和数据
    public R<T> success(T data){
        R<T> R=new R();
        R.setCode(ResultCode.SUCCESS.code);
        R.setMsg(ResultCode.SUCCESS.msg);
        R.setData(data);
        return R;
    }

    //失败，返回自己定义的信息码和信息
    public R<T> error(){
        R<T> R=new R<>();
        R.setCode(ResultCode.ERROR.code);
        R.setMsg(ResultCode.ERROR.code);
        return R;
    }

    //失败，返回controller层传过来信息码和信息
    public R<T> error(String code,String msg){
        R<T> R=new R<>();
        R.setCode(code);
        R.setMsg(msg);
        return R;
    }

}