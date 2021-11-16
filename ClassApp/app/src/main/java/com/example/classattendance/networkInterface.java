package com.example.classattendance;

import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface networkInterface {
    @GET("/attendance")
    Call<JsonObject> solve(
            @Query("image")String method
    );
    @GET("/register")
    Call<JsonObject> reg(
            @Query("image")String method,
            @Query("phone")String method1
    );
}
