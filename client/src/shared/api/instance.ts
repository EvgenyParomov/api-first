const baseURL = "/api"; // use your own URL here or environment variable

export const apiInstance = async <T>({
  url,
  method,
  params,
  data,
  headers,
  signal,
}: {
  url: string;
  method: "GET" | "POST" | "PUT" | "DELETE" | "PATCH";
  params?: string[][] | Record<string, string> | string | URLSearchParams;
  data?: BodyType<unknown>;
  signal?: AbortSignal;
  headers?: HeadersInit;
  responseType?: string;
}): Promise<T> => {
  const response = await fetch(
    `${baseURL}${url}` + new URLSearchParams(params),
    {
      method,
      headers,
      signal,
      ...(data ? { body: JSON.stringify(data) } : {}),
    }
  );

  return response.json();
};

export default apiInstance;

export type BodyType<BodyData> = BodyData;
